from rest_framework import serializers
from .models import Home

#specifies the model to work with and the fields to be converted to JSON.
class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'title', 'description', 'completed')