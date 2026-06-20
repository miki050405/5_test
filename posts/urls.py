from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListCreateApiView.as_view()),
    path('<int:id>/', views.PostDetailApiView.as_view()),
    path('<int:id>/comments/', views.CommentListCreateApiView.as_view()),
]