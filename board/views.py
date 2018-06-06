from django.shortcuts import render
from django.views.generic import ListView
from board.models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article
