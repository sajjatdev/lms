from pyexpat import model
from rest_framework import serializers
from . import models
class AuthorSerializer(serializers.ModelSerializer):
               
         class Meta:
               model=models.Author
               fields="__all__"
