"""apiConDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from appApi import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("create_user/", views.create_user, name="create_user"),
    path("get_user_by_id/<int:id>", views.get_user_by_id, name="get_user_by_id"),
    path("get_users/", views.get_users, name="get_users"),
    path("update_user/<int:id>", views.update_user, name="update_user"),
    path("delete_user/<int:id>", views.delete_user, name="delete_user"),
]
