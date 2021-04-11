from django.db import models

# Create your models here.

class Publisher(models.Model):
    publisher_id = models.CharField(max_length=64, unique=True)
    pub_name = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)

class Book(models.Model):
    book_id = models.CharField(max_length=64, unique=True)
    book_name = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    pub_date = models.CharField(max_length=32)
    publisher_id = models.ForeignKey('Publisher', on_delete=models.CASCADE)
