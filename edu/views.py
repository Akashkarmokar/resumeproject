from django.shortcuts import render

# Create your views here.

def skill(request):
    data = {'skill':'active'}
    return render(request,'edu/skill.html',data)