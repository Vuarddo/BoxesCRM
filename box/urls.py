from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('box/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
