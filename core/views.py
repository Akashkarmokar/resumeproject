from django.shortcuts import render

# Create your views here.
def home(request):
    data = {'home':'active'}
    return render(request,'core/home.html',data)

def contact(request):
    data = {'contact':'active'}
    return render(request,'core/contact.html',data)