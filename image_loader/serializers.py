from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Image

User = get_user_model()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
