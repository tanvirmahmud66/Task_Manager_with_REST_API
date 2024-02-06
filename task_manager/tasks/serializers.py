from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tasks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name','last_name','password')
        extra_kwargs = {'password': {'write_only': True}}
        required_fields = ['username', 'email', 'first_name','last_name','password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
