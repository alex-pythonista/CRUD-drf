from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import StudentInfo
from .serializers import StudentInfoSerializer

@api_view(['GET'])
def home(request):
    student_objs = StudentInfo.objects.all()
    serializer = StudentInfoSerializer(student_objs, many=True)

    return Response({'status': 200, 'payload': serializer.data})

@api_view(['POST'])
def post_student(request):
    # data = request.data
    serializer = StudentInfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'saved to database'})
    else:
        return Response({'status': 403, 'errors': serializer.errors, 'payload': request.data})