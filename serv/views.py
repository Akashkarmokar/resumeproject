from django.shortcuts import render

# Create your views here.

def services(request):
    data = {'services':'active'}
    return render(request,'serv/services.html',data)
