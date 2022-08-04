from django.test import TestCase
from .models import Post

# Create your tests here.

class TestAppModels(TestCase):

    def test_model_str(self):
        name = Post.objects.create(name="Django Testing")
        self.assertEqual(str(name), "Django Testing")
        