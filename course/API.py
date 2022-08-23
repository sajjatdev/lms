from rest_framework import serializers
from . import models

class courseSerializer(serializers.ModelSerializer):
               class Meta:
                     model= models.Course
                     fields="__all__"