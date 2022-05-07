from dataclasses import field
from unicodedata import category

from .models import Category, StudentInfo, Book
from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
        

class StudentInfoSerializer(ModelSerializer):

    class Meta:
        model = StudentInfo
        fields = ['id', 'name', 'age', 'school']
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