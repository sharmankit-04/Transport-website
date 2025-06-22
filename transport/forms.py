from django import forms
from .models import Booking
from .models import Inquiry
from .locations import LOCATIONS


# from .forms import BookingForm, InquiryForm, TrackingForm  # Remove ReviewForm if not needed

def my_view(request):
    from .forms import BookingForm, InquiryForm, TrackingForm, ReviewForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'customer_name', 'pickup_location', 'delivery_location',
            'goods_type', 'truck_type', 'contact_number'
        ]

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your message here...'}),
        }


class TrackingForm(forms.Form):
    tracking_number = forms.CharField(label='Tracking Number', max_length=100)


class TrackShipmentForm(forms.Form):
    tracking_number = forms.CharField(max_length=100, label="Tracking Number")


# forms.py

class DeliveryEstimateForm(forms.Form):
    pickup_location = forms.ChoiceField(
        choices=LOCATIONS,
        widget=forms.Select(attrs={
            'class': 'form-select form-select-lg',
        }),
        label="Pickup Location"
    )
    delivery_location = forms.ChoiceField(
        choices=LOCATIONS,
        widget=forms.Select(attrs={
            'class': 'form-select form-select-lg',
        }),
        label="Delivery Location"
    )
    goods_type = forms.ChoiceField(
        required=False,
        choices=[
            ('', '-- Select Goods Type --'),
            ('Electronics', 'Electronics'),
            ('Furniture', 'Furniture'),
            ('Clothing', 'Clothing'),
            ('Food', 'Food'),
            ('Automotive', 'Automotive'),
            ('Others', 'Others'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select form-select-lg',
        }))