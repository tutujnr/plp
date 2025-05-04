from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreate.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('tasks/', views.TaskListCreate.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
]