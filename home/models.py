from django.db import models


class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=18)
    school = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
