import hashlib

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from . serializers import UserSerializer


class UserOp(APIView):

    def get(self, request):
        users=User.objects.all()
        serializer=UserSerializer(users, many=True)
        return Response({"users": serializer.data})


    def post(self,request):
        if (User.objects.filter(email=request.POST['email']).exists()):
            return Response({'response': 'exists'})

        else:
            user = User.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                password=hashlib.md5(request.POST['password'].encode()).hexdigest()
            )
            user.save()
            return Response({'response': 'success'})


class UserLogin(APIView):

    def post(self, request):
        if (User.objects.filter(email=request.POST['email']).exists()):
            user = User.objects.filter(email=request.POST['email'])[0]
            password = hashlib.md5(request.POST['password'].encode()).hexdigest()
            if(user.password==password):
                return Response({"response": "success"})
            else:
                return Response({"response": "wrong_pass"})

        else:
            return Response({"response": "404"})



