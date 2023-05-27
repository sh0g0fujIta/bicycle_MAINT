from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
    path('', views.template_view, name='list'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.singup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
