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
    path('list/', views.list_view, name='list'),
    path('bicycle_create/', views.bicycle_create_view, name='bicycle_create'),
    path('bicycle_detail/<int:bicycle_id>', views.bicycle_detail_view, name='bicycle_detail'),
    path('bicycle_delete/<int:bicycle_id>', views.bicycle_delete_view, name='bicycle_delete'),
    path('part_create/<int:bicycle_id>', views.part_create_view, name='part_create'),
    path('part_delete/<int:part_id>', views.part_delete_view, name='part_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)