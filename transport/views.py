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
from .forms import DeliveryEstimateForm


import os
import joblib
import pandas as pd

# 📍 Load ML Model once globally
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'delhi_bombay_roadlines', 'ml_models', 'freight_price_model.pkl')
freight_model = joblib.load(MODEL_PATH)

# Debug/Test View
def test_view(request):
    return HttpResponse("Hello, DEBUG is on.")

# Home Page (Just UI)
def home(request):
    return render(request, 'transport/home.html')

# Booking Page
@login_required
def booking(request):
    if request.method == 'POST':
        Booking.objects.create(
            customer_name=request.POST.get('customer_name'),
            contact_number=request.POST.get('contact_number'),
            pickup_location=request.POST.get('pickup_location'),
            delivery_location=request.POST.get('delivery_location'),
            goods_type=request.POST.get('goods_type'),
            truck_type=request.POST.get('truck_type'),
            status='Pending'
        )
        messages.success(request, "Booking submitted successfully!")
        return redirect('booking')
    return render(request, 'transport/booking_new.html')

# Admin Dashboard
@login_required
def admin_dashboard(request):
    bookings = Booking.objects.all()
    trucks = Truck.objects.all()
    booking_paginator = Paginator(bookings, 10)
    truck_paginator = Paginator(trucks, 5)
    page_number = request.GET.get('page', 1)
    return render(request, 'transport/admin_dashboard.html', {
        'bookings': booking_paginator.get_page(page_number),
        'trucks': truck_paginator.get_page(page_number)
    })

# Static Pages
def about(request):
    return render(request, 'transport/about.html')

def contact(request):
    return render(request, 'transport/contact.html')

# User Registration
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('home')
    return render(request, 'transport/register.html', {'form': form})

# Login View
def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        messages.success(request, f"Welcome back, {user.username}!")
        return redirect('home')
    elif request.method == 'POST':
        messages.error(request, "Invalid credentials")
    return render(request, 'transport/login.html', {'form': form})

# Logout
def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')

# Shipment Tracking
def track_shipment(request):
    shipment = None
    form = TrackShipmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        tracking_number = form.cleaned_data['tracking_number']
        try:
            shipment = Shipment.objects.get(tracking_number=tracking_number)
        except Shipment.DoesNotExist:
            shipment = None
    return render(request, 'transport/track_shipment.html', {'form': form, 'shipment': shipment})

# Predict Freight Price
def predict_price(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        distance = float(request.POST['distance'])
        vehicle_type = request.POST['vehicle_type']

        df = pd.DataFrame([[weight, distance, vehicle_type]], columns=['weight', 'distance', 'vehicle_type'])
        try:
            price = freight_model.predict(df)[0]
            return render(request, 'transport/price_result.html', {'price': round(price, 2)})
        except Exception as e:
            return HttpResponse(f"Error in prediction: {e}")
    return render(request, 'transport/predict_price.html')

# Inquiry Form (Separate Page)
def inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'transport/inquiry_success.html')  # ⬅️ Success page
    else:
        form = InquiryForm()
    return render(request, 'transport/inquiry.html', {'form': form})

# transport/views.py


# transport/views.py

from django.shortcuts import render
from .forms import DeliveryEstimateForm

# Dummy distance data for example:
DISTANCE_MAP = {
    ('Delhi', 'Mumbai'): 1400,
    ('Mumbai', 'Delhi'): 1400,
    ('Delhi', 'Chennai'): 2200,
    ('Chennai', 'Delhi'): 2200,
    ('Mumbai', 'Pune'): 150,
    ('Pune', 'Mumbai'): 150,
    ('Delhi', 'Jaipur'): 280,
    ('Jaipur', 'Delhi'): 280,
    # aur add kar sakta hai jitna chahiye
}

def estimate_delivery(request):
    estimated_days = None
    if request.method == 'POST':
        form = DeliveryEstimateForm(request.POST)
        if form.is_valid():
            pickup = form.cleaned_data['pickup_location']
            delivery = form.cleaned_data['delivery_location']
            goods_type = form.cleaned_data.get('goods_type')

            # Distance lookup from map
            distance = DISTANCE_MAP.get((pickup, delivery))
            if not distance:
                distance = DISTANCE_MAP.get((delivery, pickup), None)

            # Agar distance na mile to default
            if not distance:
                estimated_days = 7  # default 7 days agar unknown route
            else:
                # Assume 500 km per day delivery speed
                days = distance / 500

                # Goods type se thoda adjust karo
                if goods_type:
                    if 'fragile' in goods_type.lower():
                        days += 1
                    elif 'electronics' in goods_type.lower():
                        days += 0.5

                estimated_days = int(days) if days.is_integer() else int(days) + 1
    else:
        form = DeliveryEstimateForm()

    return render(request, 'transport/estimate_delivery.html', {
        'form': form,
        'estimated_days': estimated_days,
    })
