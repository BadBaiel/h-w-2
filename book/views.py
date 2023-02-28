from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from .forms import CommentForm
from django.views import generic
from django.views.generic import DetailView, CreateView
# Create your views here.

class BookView(generic.ListView):
    template_name = 'book.html'
    queryset = models.Book.objects.all()
    def get_queryset(self):
        return models.Book.objects.all()

class BookDetailView(generic.DetailView, ):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)


class BookCreateView(generic.CreateView):
    template_name = 'add-book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/book/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)

class BookUpdateView(generic.UpdateView):
    template_name = 'update-book.html'
    form_class = forms.BookForm
    success_url = '/book/'
    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)

class BookDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/book/'
    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=show_id)


# def book_view(request):
#     book = models.Book.objects.all()
#     return render(request, 'book.html', {'book': book})
# def book_detailview(request, id, self, **kwargs):
#     book_id = get_object_or_404(models.Book, id=id)
#     return render(request, 'book_detail.html', {'book_id': book_id})
#     context = super().get_context_data(**kwargs)
#     context["star_form"] = RatingForm()
#     return context
#
#
# def create_book_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2>Фильм добавлен можешь собой гордится!</h2>')
#     else:
#         form = forms.BookForm()
#     return render(request, 'add-book.html', {'form': form})
#
# def update_book_view(request, id):
#     show = get_object_or_404(models.Book, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(instance=show, data=request.POST)
#         if form.is_valid():
#             form.save()
#         return HttpResponse("<h2>Фильм успешно обновлен!</h2>")
#     else:
#         form = forms.BookForm(instance=show)
#
#     return render(request, 'update-book.html', {'form': form,
#                                                 'object': show})
#
# def delete_book_view(request, id):
#     show_object = get_object_or_404(models.Book, id=id)
#     show_object.delete()
#     return HttpResponse('<h2>Фильм успешно удален</h2>')
#
#
#
# class AddStarRating(View):
#     def get_client_ip(self, request):
#         x_forwarded_for = request.Meta.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.Meta.get('REMOTE_ADDR')
#         return ip
#
#     def post(self, request):
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             Rating.objects.update_or_create(
#                 ip=self.get_client_ip(request),
#                 book_id=int(request.POST.get("movie")),
#                 defaults={'star_id': int(request.POST.get('star'))})
#
#             return HttpResponse(status=201)
#         else:
#             return HttpResponse(status=400)