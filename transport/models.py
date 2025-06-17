from django.db import models
from django.contrib.auth.models import User


# Booking model with relevant fields
class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=200)
    delivery_location = models.CharField(max_length=200)
    goods_type = models.CharField(max_length=100)
    truck_type = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the time when the booking is created

    def __str__(self):
        return f"{self.customer_name} - {self.pickup_location} to {self.delivery_location}"


# Truck model for truck information
class Truck(models.Model):
    truck_type = models.CharField(max_length=50)
    availability_status = models.CharField(max_length=20, default='Available')

    def __str__(self):
        return self.truck_type


# Inquiry model for customer inquiries
class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


# Shipment model to track shipments
class Shipment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)  # Link to the booking
    tracking_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=100)
    current_location = models.CharField(max_length=100)
    estimated_delivery_date = models.DateField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tracking Number: {self.tracking_number}"


