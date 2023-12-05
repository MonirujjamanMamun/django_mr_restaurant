from django.shortcuts import render

# Create your views here.
def aboutUs(request):
    return render(request, 'aboutUs.html')
