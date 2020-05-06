from django.db import models


class Post(models.Model):
    title = models.CharField('title', max_length=255)

    def __str__(self):
        return self.title
