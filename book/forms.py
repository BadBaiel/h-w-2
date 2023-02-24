from django import forms
from . import models
from .models import Book, Rating, Ratingstar

class BookForm(forms.ModelForm):
    class Meta:
        model= models.Book
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("name", "email", "text")

class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=Ratingstar.objects.all(), widget=forms.RadioSelect(), empty_label=None

    )

    class Meta:
        model = Rating
        fields = ("star",)