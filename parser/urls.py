from django.urls import path
from . import views

app_name = 'parse'
urlpattern = [
    path('film_list', views.ParserView.as_view(), name='film_list'),
    path('parsing/', views.ParserFormView.as_view(), name='parser_film')
]