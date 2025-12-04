from rest_framework import serializers
from .models import Student

# 3) CUSTOM VALIDATION (Global validation function)
def validate_city(value):
    if value.lower() not in ["kathmandu", "banepa", "dulikhel"]:
        raise serializers.ValidationError("City must be Kathmandu, Banepa, or Dulikhel.")
    return value


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100, validators=[validate_city])

    # 1) FIELD LEVEL VALIDATION
    def validate_name(self, value):
        """Field level validation for name"""
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value

    def validate_roll(self, value):
        """Field level validation for roll"""
        if value <= 0:
            raise serializers.ValidationError("Roll must be a positive number.")
        return value

    # 2) OBJECT LEVEL VALIDATION
    def validate(self, data):
        """Object level validation for checking full data"""
        name = data.get("name")
        city = data.get("city")

        if city.lower() == "kathmandu" and name.lower().startswith("x"):
            raise serializers.ValidationError("Name cannot start with 'X' for Kathmandu students.")

        return data

    # CREATE METHOD
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # UPDATE METHOD
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance