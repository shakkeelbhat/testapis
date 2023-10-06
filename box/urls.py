from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.registerApi.as_view()),
    path('login/',views.loginApi.as_view()),
    path('list/', views.listApi.as_view()),
    path('add/', views.addApi.as_view()),
]