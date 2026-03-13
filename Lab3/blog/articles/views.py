from django.shortcuts import render
from .models import Article
from django.http import Http404
from django.shortcuts import redirect

def create_post(request):
    if request.user.is_anonymous:
        raise Http404("Требуется авторизация")

    if request.method == "POST":
        form = {
            'title': request.POST.get("title", ""),
            'text': request.POST.get("text", ""),
            'errors': ""
        }
        if not form['title'] or not form['text']:
            form['errors'] = "Не все поля заполнены"
            return render(request, "create_post.html", {"form": form})
        # Создаем новую статью
        article = Article.objects.create(
            title=form['title'],
            text=form['text'],
            author=request.user
        )
        return redirect('get_article', article_id=article.id)
    else:
        return render(request, "create_post.html", {})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найдена")
    return render(request, "article.html", {"post": post})


def archive(request):
    posts = Article.objects.all()
    return render(request, "archive.html", {"posts": posts})

# Create your views here.
