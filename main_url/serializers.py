from rest_framework import serializers
 
from .models import *
from .serializers import * 
 
class UrlSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =urls
        fields = '__all__'
