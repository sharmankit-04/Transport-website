from django.contrib import admin
from django.urls import path
from transport import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('booking/', views.booking, name='booking'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('track/', views.track_shipment, name='track_shipment'),
    path('predict-price/', views.predict_price, name='predict_price'),
    path('inquiry/', views.inquiry_view, name='inquiry'),
    path('estimate-delivery/', views.estimate_delivery, name='estimate_delivery'),
]
