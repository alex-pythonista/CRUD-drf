from urllib import request
from django.db import models
from pkg_resources import require


class StudentInfo(models.Model):
    name = models.CharField(max_length=100, default='')
    age = models.PositiveIntegerField(default=18)
    school = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name