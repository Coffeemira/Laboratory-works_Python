from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Article

def archive(request):
    posts = Article.objects.all()
    return render(request, 'archive.html', {"posts": posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404("Статья не найдена")

@login_required
def create_post(request):
    if request.method == "POST":
        form = {
            'text': request.POST.get("text", ""),
            'title': request.POST.get("title", "")
        }
        if form["text"] and form["title"]:
            try:
                article = Article.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )
                return redirect('get_article', article_id=article.id)
            except Exception as e:
                form['errors'] = "Ошибка при сохранении: возможно, статья с таким названием уже существует."
                return render(request, 'create_post.html', {'form': form})
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        return render(request, 'create_post.html', {})