from rest_framework import serializers
from .models import Freeboard, Freeboard_comment


class FreeboardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freeboard
        fields = '__all__'
        
    
class FreeboardcommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freeboard_comment
        fields = '__all__'


