from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path("listings/",   views.listings_page, name="listings"),
  path("listings/<int:pk>/", views.listing_detail, name="listing_detail"),

]