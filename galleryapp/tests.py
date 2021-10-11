from django.test import TestCase
from .models import Location, Category, Image

class ImageTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        Image.objects.create(
            name="Test Image",
            description="Test Description",
            location=Location.objects.create(name="Test Location"),
            category=Category.objects.create(name="Test Category"),
            image="http://tests.com/test.jpg",
            created_at=None
        )

    def test_image_name(self):
        """
        Test the image name
        """
        image = Image.objects.get(name="Test Image")
        self.assertEqual(image.name, "Test Image")    
        
    def test_image_category(self):
        """
        Test that the image category is correct
        """
        image = Image.objects.get(name="Test Image")
        self.assertEqual(image.category.name, "Test Category")

    def test_image_image(self):

        image = Image.objects.get(name="Test Image")
        self.assertEqual(image.image, "http://test.com/test.jpg")

    