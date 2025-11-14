from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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

def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", ""),
            'email': request.POST.get("email", ""),
            'password': request.POST.get("password", "")
        }
        if form["username"] and form["email"] and form["password"]:
            try:
                user = User.objects.get(username=form["username"])
                form['errors'] = "Пользователь с таким логином уже существует."
                return render(request, 'register.html', {'form': form})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=form["username"],
                    email=form["email"],
                    password=form["password"]
                )
                login(request, user)
                return redirect('archive')
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {})

def user_login(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", ""),
            'password': request.POST.get("password", "")
        }
        if form["username"] and form["password"]:
            user = authenticate(username=form["username"], password=form["password"])
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                form['errors'] = "Неверный логин или пароль"
                return render(request, 'login.html', {'form': form})
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {})