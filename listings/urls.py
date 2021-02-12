from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'), # display the listing page using the index method defined in listings/views
    path('<int:listing_id>', views.listing, name='listing'), # views.listing is the function in listing/views and int:listing_id is for the parameters
    path('search', views.search, name='search'),
]

