from django import forms
from .models import Booking

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

class InquiryForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class TrackingForm(forms.Form):
    tracking_number = forms.CharField(label='Tracking Number', max_length=100)


class TrackShipmentForm(forms.Form):
    tracking_number = forms.CharField(max_length=100, label="Tracking Number")
