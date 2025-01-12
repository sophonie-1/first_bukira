from rest_framework import serializers
from .models import Booking,Menu
from django.contrib.auth.models import User


from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')

class Login(serializers.Serializer):
    name =serializers.CharField()
    password = serializers.CharField(write_only=True)
    
class RegisterUser(serializers.Serializer):
    username = serializers.CharField()
    email =serializers.EmailField()
    password =serializers.CharField(write_only=True)
    
    def validate(self, data):
        characters ="!@#$%^&*()~`.,<>?/}|"
        if data:
            if any(c in characters for c in data['username']):
                raise serializers.ValidationError("you can not use special characters in username!")
            elif User.objects.filter(username =data['username']).exists():
                raise serializers.ValidationError("username has ready taken")
            elif User.objects.filter(email =data['email']).exists():
                raise serializers.ValidationError("email has read taken in use!")
        return data
    
        



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"