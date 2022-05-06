from dataclasses import field
from unicodedata import category
from .models import Category, StudentInfo, Book
from rest_framework.serializers import ModelSerializer, ValidationError


class StudentInfoSerializer(ModelSerializer):

    class Meta:
        model = StudentInfo
        fields = ['name', 'age']
        # exclude = [field's name,]

    def validate(self, data):
        """
        Write all the custom validation overriding the .validate() method
        In DRF, the validation part is entirely done inside the serializer
        class.
        """
        if data['age'] < 18:
            raise ValidationError({'error': 'age cannot be less than 18'})

        return data


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['name',]


class BookSerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = ['name', 'category']