from django.shortcuts import render, get_object_or_404
from .models import Listing

def home(request):
    return render(request, "listings/index.html")


def about(request):
    return render(request, "listings/about.html")

def listings_page(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings": listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "listing_detail.html", {"listing": listing})
