from django.urls import path
from .views import postDetail, postList

urlpatterns = [
    path('posts/', postList.as_view(), name='post-list'),
    path('posts/<int:pk>/', postDetail.as_view(), name='post-detail'),
]
