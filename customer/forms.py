from django import forms
from .models import Profile, BookInterest
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'interest')

def __init__(self, *args, **kwargs):
    """Add placeholder for form fields"""

    super().__init__(*args, **kwargs)
    placeholders = {

        "full_name": "Full Name",  
        "email": "Your Email", 
        "phone_number": "Phone Number", 
        "address1": "Address Line 1", 
        "address2": "Address Line 2", 
        "postcode": "Postcode", 
        "country": "Country",
        
    }

class BookInterestForm(forms.ModelForm):
    class Meta:
        model = BookInterest
        fields = ['book_name', 'description',]


def __init__(self, *args, **kwargs):
    """Add placeholder for form fields"""

    super().__init__(*args, **kwargs)
    placeholders = {

        "book_name": "book_name",  
        "description": "description", 
    
    }   
    
