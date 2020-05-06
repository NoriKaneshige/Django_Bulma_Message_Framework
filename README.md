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

```

> ## urls.py
``` python

```

> ## profile_list.html
``` python

```
