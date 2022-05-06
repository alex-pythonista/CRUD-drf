from .models import StudentInfo
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