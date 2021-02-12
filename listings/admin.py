from django.contrib import admin

from .models import Listing

# class listingAdmin, add more information 
# to the table/list of property on the admin page
class ListingAdmin(admin.ModelAdmin):
    # the new list to display on the page
    list_display = ('id', 'title', 'is_published', 'price', 'list_date',  'realtor')
    # made the id and titile link to the property detail page
    list_display_links = ('id', 'title')
    # adding a filter box
    list_filter = ('realtor', )
    # made the is_published field editable, it is a boolena which show as a tick box on the page
    list_editable = ('is_published',)
    # add a search filed
    search_fields = ('title', 'description', 'address', 'zipcode', 'city', 'price')
    # add a maximun of property shown per page
    list_per_page = 25



# add the ListingAdmin so the admin 
# page so it get generated
admin.site.register(Listing, ListingAdmin)

