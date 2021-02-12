from django.contrib import admin

from .models import Realtor


# class RealtorAdmin, add more information 
# to the table/list of property on the admin page
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

# add the RealtorAdmin so the admin 
# page so it get generated
admin.site.register(Realtor, RealtorAdmin)
