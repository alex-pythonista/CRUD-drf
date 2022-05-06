from django.contrib import admin

from home.models import Category, StudentInfo, Book

admin.site.register(StudentInfo)
admin.site.register(Book)
admin.site.register(Category)