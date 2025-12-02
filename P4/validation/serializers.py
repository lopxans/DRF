from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Field-level validations
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Name must be at least 3 characters.')
        return value
    
    def validate_roll(self, value):
        if value >= 1000:
            raise serializers.ValidationError('Roll number must be between 1 and 1000.')
        if value <= 0:
            raise serializers.ValidationError('Roll must be positive.')
        return value
    
    def validate_city(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('City name must be at least 3 characters.')
        return value

    # Object Level Validation
    def validate(self, data):
        name = data.get('name')
        roll = data.get('roll')
        city = data.get('city')
        
        if name and city and name.lower() == city.lower():
            raise serializers.ValidationError("Name and city cannot be the same.")

        if roll and (roll <= 0 or roll > 1000):
            raise serializers.ValidationError("Roll number must be between 1 and 1000.")

        if name and len(name) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")

        return data
    
    