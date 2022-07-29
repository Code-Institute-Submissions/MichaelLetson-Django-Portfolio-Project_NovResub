from .models import Post
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'location', 'price', 'featured_image', 'content')