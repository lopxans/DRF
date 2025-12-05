from rest_framework import serializers
from .models import Student

# 3) CUSTOM VALIDATION (Global validation function)
def validate_city(value):
    if value.lower() not in ["kathmandu", "banepa", "dulikhel"]:
        raise serializers.ValidationError("City must be Kathmandu, Banepa, or Dulikhel.")
    return value

class StudentSerializer(serializers.ModelSerializer):
    # roll = serializers.IntegerField(read_only=True)
    city = serializers.CharField(validators=[validate_city])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['roll', 'city']
        # extra_kwargs = {'roll': {'ready_only': True}}

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