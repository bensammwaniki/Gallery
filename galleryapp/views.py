from django.shortcuts import render
from .models import Image, Location, Category

# Create your views here.
def home(request):
    dispimages = Image.objects.all().order_by('-id')
    dispBylocation = Location.objects.all()
    dispBycategory = Category.objects.all()

    return render(request, "index.html", {'images': dispimages, 'locations': dispBylocation, 'categories': dispBycategory})