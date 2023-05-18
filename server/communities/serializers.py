from rest_framework import serializers
from .models import Freeboard, Reviewboard


class FreeboardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freeboard
        fields = '__all__'
        
    
class ReviewboardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewboard
        fields = '__all__'


