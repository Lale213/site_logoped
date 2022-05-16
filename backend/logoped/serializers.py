
from rest_framework import serializers

from logoped.models import *


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
