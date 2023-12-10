from django.shortcuts import render, get_object_or_404
from .models import Profile, BookInterest
from .forms import ProfileForm, BookInterestForm
# Create your views here.

def show_profile(request):
    """Render user profile"""
    
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    order = profile.orders.all()
    bookinterest = get_object_or_404(BookInterest, profile=profile)
    bookform = BookInterestForm(instance=bookinterest)


    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        form.save()
        bookform = BookInterestForm(request.POST, instance=bookinterest)
        bookform.save()


    template = "customer/profile.html"
    context ={
        "form": form,
        "profile": profile,
        "order": order, 
        'bookform': bookform,
    }
    return render(request, template, context)

def test(request):
    template = "customer/test.html"
    return render(request, template)