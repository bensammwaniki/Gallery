from django.shortcuts import render
from .models import Image, Location, Category

# Create your views here.
def home(request):
    dispimages = Image.objects.all().order_by('id')
    dispBylocation = Location.objects.all()
    dispBycategory = Category.objects.all()


    return render(request, "index.html", {'images': dispimages, 'locations': dispBylocation, 'categories': dispBycategory})

def image(request, image_id):
    modimage = Image.objects.get(id=image_id)
    modtitle = image
    return render(request, 'index.html', {'image': modimage, 'title': modtitle})


def search(request):
    if 'search' in request.GET and request.GET["search"]:
        # search by lowercase
        searched_term = request.GET.get("search").lower()
        searched_images = Image.filter_by_category(searched_term)
        message = f"{searched_term}"
        locations = Location.objects.all()

        return render(request, 'result.html', {"message": message, "images": searched_images, 'locations': locations})

    else:
        locations = Location.objects.all()
        message = "Sorry we have found '0' search result"
        return render(request, 'result.html', {"message": message, 'locations': locations})   

