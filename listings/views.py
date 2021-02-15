from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

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

    # show a 404 if page doesn't exist
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords) # looking if the description contains the keywords

    # City
    if 'city' in request.GET:
        keywords = request.GET['city']
        if keywords:
            queryset_list = queryset_list.filter(city__iexact = keywords) # looking if the city field contains the exact keywords

    # State
    if 'state' in request.GET:
        keywords = request.GET['state']
        if keywords:
            queryset_list = queryset_list.filter(state__iexact = keywords) # looking if the state field contains the exact keywords

    # Bedroom
    if 'bedrooms' in request.GET:
        keywords = request.GET['bedrooms']
        if keywords:
            queryset_list = queryset_list.filter(bedrooms__lte = keywords) # looking if the bedroom field is less than keywords

    # Price
    if 'price' in request.GET:
        keywords = request.GET['price']
        if keywords:
            queryset_list = queryset_list.filter(price__lte = keywords) # looking if the price field up to keywords


    context = {
        'state_choices': state_choices, # for the dynamic search field 
        'bedroom_choices': bedroom_choices, 
        'price_choices': price_choices,
        'listings': queryset_list, # to do the search
        'values': request.GET # to keep the search input into the field
    }

    return render(request, 'listings/search.html', context)