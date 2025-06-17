from django import forms
from .models import Booking  # Import the Booking model

class BookingForm(forms.ModelForm):  # Inherit from ModelForm instead of Form
    class Meta:
        model = Booking  # Link the form to the Booking model
        fields = [
            'customer_name',
            'pickup_location',
            'delivery_location',
            'goods_type',
            'truck_type',
            'contact_number'
        ]  # Specify the fields to include in the form

class InquiryForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
