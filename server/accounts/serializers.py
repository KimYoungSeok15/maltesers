from rest_framework import serializers
from .models import Profile, Following, UserLikeGenre, UserLikeMovie


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        

class followingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'
    

class UserLikeGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLikeGenre
        fields = '__all__'

class UserLikeMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLikeMovie
        fields = '__all__'
    


