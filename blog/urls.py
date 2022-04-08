from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', include('single_pages.urls')),
    path('category/<str:slug>/', views.show_category_posts)
]