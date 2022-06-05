from app1.models import Emplo
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emplo
        fields = '__all__'