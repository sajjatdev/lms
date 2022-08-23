from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .API import courseSerializer
from .models import Course
class CourseModelViewset(ModelViewSet):
            serializer_class = courseSerializer 
            queryset=Course.objects.all()
         