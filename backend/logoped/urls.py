from django.urls import path

from .views import *


urlpatterns = [

    path('', LogopedHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PublicationCategory.as_view(), name='category'),

]
