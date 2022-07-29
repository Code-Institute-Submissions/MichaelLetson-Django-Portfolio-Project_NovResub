from .models import Post
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'name',
            'featured_image',
            'location',
            'price',
            'content',
            )

