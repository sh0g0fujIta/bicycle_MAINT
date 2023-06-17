from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "App"

urlpatterns = [
    path('', views.template_view, name='list'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.singup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('mainpage/', views.mainpage_view, name='mainpage')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)