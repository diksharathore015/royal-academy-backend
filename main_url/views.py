from django.shortcuts import render
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from django.utils.text import slugify
from django import forms
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
# View to get all courses
# views.py
from .serializers import *
from django.db.models import Prefetch
from django.http import JsonResponse
 
# Create your views here.
class URlView(ModelViewSet):
        queryset = urls.objects.all()
        serializer_class = UrlSerializer
        http_method_names = ['get', 'post', 'patch', 'delete']  # Allow GET, POST, PATCH, DELETE (optional)
      