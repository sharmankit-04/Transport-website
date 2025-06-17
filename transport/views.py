from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .decorators import login_required_with_message
from .forms import BookingForm, InquiryForm, TrackShipmentForm, TrackingForm
from .models import Booking, Truck, Inquiry, Shipment

# Debug/Test view
def test_view(request):
    return HttpResponse("Hello, DEBUG is on.")

# Home page with inquiry form and dynamic reviews
def home(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            Inquiry.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, "Your message has been sent!")
            return redirect('home')
    else:
        form = InquiryForm()
    return render(request, 'transport/home.html', {'form': form})

# ✅ Booking page — Final Correct Version
@login_required
def booking(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        contact_number = request.POST.get('contact_number')
        pickup_location = request.POST.get('pickup_location')
        delivery_location = request.POST.get('delivery_location')
        goods_type = request.POST.get('goods_type')
        truck_type = request.POST.get('truck_type')

        # Save to Booking model
        Booking.objects.create(
            customer_name=customer_name,
            contact_number=contact_number,
            pickup_location=pickup_location,
            delivery_location=delivery_location,
            goods_type=goods_type,
            truck_type=truck_type,
            status='Pending'  # default status
        )
        messages.success(request, "Booking submitted successfully!")
        return redirect('booking')  # redirect to booking page or wherever you want

    return render(request, 'transport/booking_new.html')

# Admin dashboard
@login_required
def admin_dashboard(request):   
    bookings = Booking.objects.all()
    trucks = Truck.objects.all()

    booking_paginator = Paginator(bookings, 10)
    truck_paginator = Paginator(trucks, 5)

    page_number = request.GET.get('page', 1)
    bookings_page = booking_paginator.get_page(page_number)
    trucks_page = truck_paginator.get_page(page_number)

    return render(request, 'transport/admin_dashboard.html', {
        'bookings': bookings_page,
        'trucks': trucks_page
    })

# Static pages
def about(request):
    return render(request, 'transport/about.html')

def contact(request):
    return render(request, 'transport/contact.html')

# User Registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'transport/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, 'transport/login.html', {'form': form})

# Logout
def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')

# Shipment Tracking
def track_shipment(request):
    shipment = None
    if request.method == 'POST':
        form = TrackShipmentForm(request.POST)
        if form.is_valid():
            tracking_number = form.cleaned_data['tracking_number']
            try:
                shipment = Shipment.objects.get(tracking_number=tracking_number)
            except Shipment.DoesNotExist:
                shipment = None
    else:
        form = TrackShipmentForm()
    
    return render(request, 'transport/track_shipment.html', {'form': form, 'shipment': shipment})

# Extra registration (if needed separately)
def register(request):
    return render(request, 'transport/register.html')
