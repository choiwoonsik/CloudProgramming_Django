from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', include('single_pages.urls'))
]