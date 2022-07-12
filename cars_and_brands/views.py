from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand, Car
# Create your views here.

# /brands # a list of all the car brands
# /brands/new # form for a new car brand
# /brands/<:id> # see a specific car brand
# /brands/<:id>/edit # edit page for a specific car brand
# /brands/<:brand_id>/cars # a list of cars for a specific car brand
# /brands/<:brand_id>/cars/new # form for a new car under a specific car brand
# /brands/<:brand_id>/cars/<:car_id> # see a specific car for a specific car brand
# /brands/<:brand_id>/cars/<:car_id>/edit # edit page for a specific car under a specific car brand


def brands(request):
    brands = Brand.objects.all()
    return render(request, 'cars_and_brands/index.html', {"brands": brands})


def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars_and_brands/cars.html', {"cars": cars})
