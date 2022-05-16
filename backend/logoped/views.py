from django.db.models import Q
from rest_framework import generics
from rest_framework import viewsets
from logoped.serializers import *


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.filter(is_published=True).order_by('time_create')
    serializer_class = PublicationSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('pk')
    serializer_class = CategorySerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    lookup_field = 'publication'
    lookup_url_kwarg = 'publication'
