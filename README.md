# Django_Bulma_Message_Framework

[referred blog](https://narito.ninja/blog/detail/120/)

![message-framework-bulma](message-framework-bulma.gif)

> ## models.py
``` python
from django.db import models

class Post(models.Model):
    title = models.CharField('title', max_length=255)

    def __str__(self):
        return self.title
```

> ## admin.py
``` python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

> ## views.py
``` python
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:post_list')

    def form_valid(self, form):
        self.object = post = form.save()
        messages.info(self.request, f'New post was created! Title:{post.title} pk:{post.pk}')
        return redirect(self.get_success_url())


class PostUpdate(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:post_list')

    def form_valid(self, form):
        self.object = post = form.save()
        messages.info(self.request, f'Successfully edited! Title:{post.title} pk:{post.pk}')
        return redirect(self.get_success_url())


class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('app:post_list')

    def delete(self, request, *args, **kwargs):
        self.object = post = self.get_object()
        message = f'Successfully deleted! Title:{post.title} pk:{post.pk}'
        post.delete()
        messages.info(self.request, message)
        return redirect(self.get_success_url())
```

> ## urls.py
``` python
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('update/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name='post_delete')
]
```

> ## base.html
``` python
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
</head>
<body>
<!-- ナビバー部分 -->
<nav class="navbar is-black" role="navigation" aria-label="main navigation">
    <div class="container">
        <div class="navbar-brand">
            <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false"
               data-target="navbar-menu">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>
        <div id="navbar-menu" class="navbar-menu">
            <div class="navbar-start">
                <a class="navbar-item" href="{% url 'app:post_list' %}">Home</a>
                <a class="navbar-item" href="{% url 'app:post_create' %}">New</a>
            </div>
        </div>
</nav>

<!-- メッセージフレームワーク -->
{% if messages %}
<div class="container" style="margin-top:1rem;">
    <div class="notification is-info">
        <button class="delete" type="button"></button>
        {% for message in messages %}
        <p> {{ message }}</p>
        {% endfor %}
    </div>
</div>
{% endif %}}


<!-- メインコンテンツ -->
<main>
    {% block content %}{% endblock %}
</main>

<script>
    // notificationを×押下で閉じれるように。
    for (const element of document.querySelectorAll('.notification > .delete')) {
        element.addEventListener('click', e => {
            e.target.parentElement.classList.add('is-hidden');
        });
    }

    // ナビバーの開閉を設定
    for (const element of document.querySelectorAll('.navbar-burger')) {
        const menuId = element.dataset.target;
        const menu = document.getElementById(menuId);
        element.addEventListener('click', e => {
            element.classList.toggle('is-active');
            menu.classList.toggle('is-active');
        });
    }

</script>
</body>
</html>
```

> ## .html
``` python

```
> ## .html
``` python

```
> ## post_confirm_delete.html
``` python
{% extends 'app/base.html' %}

{% block content %}
    <section class="section">
        <div class="container">
            <form action="" method="POST">
                <p>{{ post.title }}を削除します。</p>
                <button type="submit" class="button is-danger">送信</button>
                {% csrf_token %}
            </form>
        </div>
    </section>
{% endblock %}
```
