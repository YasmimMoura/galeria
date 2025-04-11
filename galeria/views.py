from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'galeria/index.html')

def aboutus(request):
    return render(request, 'galeria/herois.html')