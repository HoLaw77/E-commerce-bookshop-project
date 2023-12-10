from django.shortcuts import render, get_object_or_404
from .models import Profile

# Create your views here.
def show_profile(request):
    """Render user profile"""
    profile = get_object_or_404(Profile, user=request.user)
    template = "profile/profile.html"
    context ={
        "profile": profile, 
    }
    return render(request, template, context)