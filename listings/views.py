from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

def index(request):
    # import the listing ordered by date, the most recent is the first
    # the filter link the admin page and the website
    # show the house only if it is published
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # adding a paginator with 3 houses form the listings per page
    paginator = Paginator(listings, 3)
    # getting the page number
    page = request.GET.get('page')
    # passing the page to the paginator
    paged_listings = paginator.get_page(page)

    # dictionary of value we want to pass to the html page
    # the html page needs to be updated in consequence
    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')