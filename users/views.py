from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserView(CreateAPIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # queryset = User.objects.all()
    # lookup_field = 'id'

# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'id'