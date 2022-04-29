from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing),
    path('about_me/', views.about_me),
    path('markdownx/', include('markdownx.urls'))
]

