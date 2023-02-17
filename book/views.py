
from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.


def book_view(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book': book})
def book_detailview(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_id': book_id})