from django.urls import path
from . import views

urlpatterns = [
    path('user', views.UserAPIView.as_view()),
    path('all-posts/', views.PostListCreateAPIView.as_view()),
    path('follow/<int:id>', views.FollowersCreateAPIView.as_view()),
    path('unfollow/<int:id>', views.FollowersDestroyAPIView.as_view()),
    path('like/<int:id>', views.LikeCreateAPIView.as_view()),
    path('likelist/', views.LikeListAPIView.as_view()),
    path('unlike/<int:id>', views.LikeDestroyAPIView.as_view()),
    path('comment/', views.CommentCreateAPIView.as_view()),
    path('comment/<int:id>', views.CommentListCreateAPIView.as_view()),
]
