from django import forms
from . import models
# from .models import Book, Rating, Ratingstar


class BookForm(forms.ModelForm):
    class Meta:
        model= models.Book
        fields = '__all__'

class CommentForm(forms.Form):
    comments = forms.CharField(min_length=3)
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ("name", "email", "text")
#
# class RatingForm(forms.ModelForm):
#     star = forms.ModelChoiceField(
#         queryset=Ratingstar.objects.all(), widget=forms.RadioSelect(), empty_label=None
#
#     )
#
#     class Meta:
#         model = Rating
#         fields = ("star",)