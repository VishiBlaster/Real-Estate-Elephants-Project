from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("listings/", views.listings_page, name="listings"),
    path("listings/<int:pk>/", views.listing_detail, name="listing_detail"),
]
