from django.http import JsonResponse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)
from board.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "board/article_list.html"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "board/article_create.html"
    fields = ["title", "content"]


class ArticleDetailView(DetailView):
    model = Article
    template_name = "board/article_detail.html"


# For API
def last_article(request):
    last_article = Article.objects.order_by('-pk')[:10].values()
    print('START')
    print(last_article)
    articles = list(last_article)
    print(articles)
    return JsonResponse(articles, safe=False)
