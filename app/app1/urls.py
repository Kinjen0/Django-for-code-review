"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    # Default view is djangos login view with a registration template for login
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('chat/', views.chat, name='chat'),
    # PAth for the edit comments, it takes in a comment id and passes it to the view
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
]
