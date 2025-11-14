from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.title