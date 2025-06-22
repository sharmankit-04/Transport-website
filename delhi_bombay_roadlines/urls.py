from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transport.urls')),  # sab route yahan se transport app me jaenge
]
