from rest_framework import serializers
from .models import Parameter
from .models import ParameterHistory


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'


class ParameterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterHistory
        fields = '__all__'



