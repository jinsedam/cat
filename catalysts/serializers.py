from rest_framework import serializers
from .models import Catalyst

class CatalystSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalyst
        fields = '__all__'