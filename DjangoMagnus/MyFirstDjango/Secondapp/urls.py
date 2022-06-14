from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special')
]