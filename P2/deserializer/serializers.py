from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    roll = serializers.IntegerField()
    city = serializers.CharField()
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)