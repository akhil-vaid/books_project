from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)
    pages = models.IntegerField()
    cover = models.ImageField(upload_to="book_covers/", blank=True, null=True)
    language = models.CharField(max_length=50)
    genre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
