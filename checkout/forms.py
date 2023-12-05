from django import forms
from .models import Order

class confirmOrder(forms.Modelform):
    class Meta:
        model = Order
        fields = ("full_name", "countries", 
    "email", "phone_number", "address1", "address2", "postcode", 
    "country")

def __init__(self, *args, **kwargs):
    """Add placeholder for form fields"""

    super().__init__(*args, **kwargs)
    placeholder(
        "full_name": "Full Name",  
        "email": "Your Email", 
        "phone_number": "Phone Number", 
        "address1": "Address Line 1", 
        "address2": "Address Line 2", 
        "postcode": "Postdode", 
        "countries": "Country",
    )
