from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "pages/home.html")

def home_redirect(request):
    return redirect("../")

def about(request):
    return render(request, "pages/about.html")
