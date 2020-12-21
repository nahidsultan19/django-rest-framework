from rest_framework import serializers
from .models import BookRest


class BookRestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRest
        fields = '__all__'
