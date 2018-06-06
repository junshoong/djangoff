from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
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
@require_http_methods(["GET"])
def last_article(request):
    articles = list(Article.objects.order_by('-pk')[:10].values())
    return JsonResponse(articles, safe=False)
