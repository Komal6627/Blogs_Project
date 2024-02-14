from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path('', home),
    path('about/', about),
    path('post/<slug:url>/',post),
    path('category/<slug:url>', category)
]