from .models import Post
from django import forms


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'location', 'price', 'content',)

        labels = {
            'name': '',
            'location': '',
            'price': 'Price per hour',
            'content': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),  # noqa
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),  # noqa
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Session price per hour'}),  # noqa
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us about you...'}),  # noqa
        }
