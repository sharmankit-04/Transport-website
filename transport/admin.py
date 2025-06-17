from django.contrib import admin
from .models import Booking, Truck, Inquiry, Shipment


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'pickup_location', 'delivery_location', 'status')
    search_fields = ('customer_name', 'pickup_location', 'delivery_location')
    list_filter = ('status',)
    ordering = ('id',)


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('id',)  # simplified


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'message')  # removed created_at


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'tracking_number', 'status')  # adjust if needed
