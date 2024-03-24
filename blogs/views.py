from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

def blog(request, id):
    return render(request, f'contents/{id}.html')
