from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "App"

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.singup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('list/<int:pk>', views.list_view, name='list'),
    path('bicycle_create/<int:pk>', views.bicycle_create_view, name='bicycle_create'),
    path('bicycle_detail/<int:pk>', views.bicycle_detail_view, name='bicycle_detail'),
    path('part_create/<int:pk>', views.part_create_view, name='part_create'),
]