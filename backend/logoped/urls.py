from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet)  # CRUD
router.register(r'publication', PublicationViewSet)  # CRUD
router.register(r'media', MediaViewSet)  # CRUD

urlpatterns = [

    path('', include(router.urls)),
    # path('prod_description/', ProductDescriptionViewSet.as_view()),
    # path('prod_description/<int:pk>/', ProductDescriptionViewSet.as_view()),
    # path('prod_description/prod<int:prod_id>/', ProductDescriptionViewSet.as_view()),

]
