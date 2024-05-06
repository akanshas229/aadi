from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from aadi_app.models import User, AuthToken
from aadi_app.serializers import UserSerializer, AuthTokenSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class AuthTokenViewSet(viewsets.ModelViewSet):
    queryset = AuthToken.objects.all()
    serializer_class = AuthTokenSerializer
    permission_classes = [IsAuthenticated]



# from django.shortcuts import render 
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import User
# from .serializers import UserSerializer
# from rest_framework import status


# #geting all users
# @api_view(['GET'])
# def user_list(request):
#     if request.method == 'GET':
#         querryset = User.objects.all()
#         serializers = UserSerializer(querryset, many = True)
#         return Response(serializers.data)
    
    
# @api_view(['GET'])
# def user_detail(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


# #create new user
# @api_view(['POST'])
# def user_create(request):
#     if request.method =='POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    
# @api_view(['GET','PUT'])
# def user_update(request, pk):
#     if request.method == 'GET':
#         querry = User.objects.get(pk =pk)
#         serializer = UserSerializer(querry)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = UserSerializer(querry, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = 201)
#         return Response(serializer.data, status=400)
    
# @api_view(['DELETE'])
# def user_delete(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)      