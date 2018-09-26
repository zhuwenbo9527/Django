from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
def index(request):
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == '123' and password =='123':
            #return HttpResponse('login success')
            return HttpResponseRedirect('/event_manage')
        else:
            return render(request,'index.html',{'error':'username or password error!'})