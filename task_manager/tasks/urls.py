from django.urls import path, include
from .views import CustomLoginView , CustomLogoutView,UserRegistrationView,HomeView, SingleTaskView, CreateTaskView, CompletedTaskView, UpdateTaskView,DeleteTaskConfirmView, PhotoCreateView, PhotoView

from django.contrib.auth.views import LoginView

urlpatterns = [

    path('', CustomLoginView.as_view(), name='login'),
    # path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),


    path('home/',HomeView.as_view(), name='home'),
    path('task-create/', CreateTaskView.as_view(), name='create-task'),
    path('task-details/<int:pk>/', SingleTaskView.as_view(), name='single-task'),
    path('task-completed/', CompletedTaskView.as_view(), name='task-completed'),
    path('task-update/<int:pk>/', UpdateTaskView.as_view(), name='update-task'),
    path('task-delete-confirm/<int:pk>/', DeleteTaskConfirmView.as_view(), name='delete-confirm'),

    path('upload-photo/<int:pk>/', PhotoCreateView.as_view(), name='upload_photo'),
    path('single-photo/<int:pk>/', PhotoView.as_view(), name='single_photo'),
] 