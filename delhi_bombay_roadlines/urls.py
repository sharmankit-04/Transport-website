from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transport.urls')),  # your app urls
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
