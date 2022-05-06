from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import StudentInfo, Book, Category
from .serializers import StudentInfoSerializer, BookSerializer, CategorySerializer

from rest_framework.views import APIView


class StudentAPI(APIView):

    def get(self, request):
        student_objs = StudentInfo.objects.all()
        serializer = StudentInfoSerializer(student_objs, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'saved to database'})
        else:
            return Response({'status': 403, 'errors': serializer.errors, 'payload': request.data})
    
    def put(self, request):
        try:
            student_obj = StudentInfo.objects.get(id=request.data['id'])
            serializer = StudentInfoSerializer(student_obj, data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'payload': serializer.data, 'message': 'saved to database'})
            else:
                return Response({'status': 403, 'errors': serializer.errors, 'payload': request.data})
        except Exception as e:
            return Response({'status': 403, 'message': 'invalid id!'})
    
    def patch(self, request):
        try:
            student_obj = StudentInfo.objects.get(id=request.data['id'])
            serializer = StudentInfoSerializer(student_obj, data=request.data, partial=True)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 200, 'payload': serializer.data, 'message': 'saved to database'})
            else:
                return Response({'status': 403, 'errors': serializer.errors, 'payload': request.data})
        except Exception as e:
            return Response({'status': 403, 'message': 'invalid id!'})

    def delete(self, request):
        try:
            student_obj = StudentInfo.objects.get(id=request.data['id'])
            student_obj.delete()

            return Response({'status': 200, 'message': 'data deleted!'})
        except Exception as e:
            return Response({'status': 403, 'message': 'invalid id'})



# @api_view(['GET'])
# def get_book(request):
#     book_objs = Book.objects.all()
#     serializer = BookSerializer(book_objs, many=True)
#     return Response({'status': 200, 'payload': serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     # data = request.data
#     serializer = StudentInfoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'message': 'saved to database'})
#     else:
#         return Response({'status': 403, 'errors': serializer.errors, 'payload': request.data})

# @api_view(['PUT', 'PATCH'])
# def update_student(request, id):
#     try:
#         student_obj = StudentInfo.objects.get(id=id)
#         serializer = StudentInfoSerializer(student_obj, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 200, 'payload': serializer.data, 'message': 'saved to database'})
#         else:
#             return Response({'status': 403, 'errors': serializer.errors, 'payload': request.data})
#     except Exception as e:
#         return Response({'status': 403, 'message': 'invalid id!'})

# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = StudentInfo.objects.get(id=id)
#         student_obj.delete()

#         return Response({'status': 200, 'message': 'data deleted!'})
#     except Exception as e:
#         return Response({'status': 403, 'message': 'invalid id'})