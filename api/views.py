from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import TaskSerializ
from .models import Task


class Index(APIView):
    def get(self, request):
        task = Task.objects.first()
        serializer = TaskSerializ(task)
        data = serializer.data
        return JsonResponse(data)
class AddTask(APIView):
    def post(self,request):
        data = request.data
        serializ =  TaskSerializ(data=data)
        print(serializ.create())

        return JsonResponse("hi",safe=False)
    