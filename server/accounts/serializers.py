from rest_framework import serializers
from .models import Profile, Following


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        

class followingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'
        
    


