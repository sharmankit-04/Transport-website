from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # ✅ Authentication paths
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # ✅ Tracking path
    path('track_shipment/', views.track_shipment, name='track_shipment'),
]
