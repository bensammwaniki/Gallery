from django.db import models
import datetime as dt

class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # save location to database
    def save_location(self):
        self.save()

    # update location
    def update_location(self, name):
        self.name = name
        self.save()

     # delete location from database
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


# category model
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def save_category(self):
        self.save()

    def update_category(self, name):
        self.name = name
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


# Image model
# =============================
class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()


    def update_image(self, name, description, location, category):
        self.name = name
        self.description = description
        self.location = location
        self.category = category
        self.save()

    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.get(id=id)
        return image

    @classmethod
    def filter_by_location(cls, location):
        images = Image.objects.filter(location__name=location)
        return images

    @classmethod
    def filter_by_category(cls, category):
        images = Image.objects.filter(category__name=category)
        return images

    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.name
