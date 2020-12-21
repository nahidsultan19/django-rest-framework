from django.db import models

# Create your models here.


class BookRest(models.Model):
    book_name = models.CharField(max_length=50)
    auth_name = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name
