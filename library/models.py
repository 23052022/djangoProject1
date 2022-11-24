from django.db import models
from django.utils.translation import gettext_lazy


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):
    class BookType(models.TextChoices):
        ukrainian = 'ukrainian', gettext_lazy('ukrainian')
        english = 'english', gettext_lazy('english')
        deutsh = 'deutsh', gettext_lazy('deutsh')

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.IntegerField()
    language = models.CharField(max_length=200, choices=BookType.choices)

class Comment(models.Model):
    name = models.CharField(max_length=30)
    id_book = models.IntegerField()
    comment = models.TextField()



