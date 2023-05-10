from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def userRegister(request):
    form=UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)        
        if form.is_valid():
            form.save()
            messages.success(request, 'Kayıt Başarılı. Giriş Yapabilirsiniz')
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'register.html',context)

def userLogin(request):
    if request.method == "POST":
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']
        
        user = authenticate(request,username=kullanici,password=sifre)

        if kullanici is not None:
            login(request,user)
            messages.success(request, 'Giriş Başarılı')
            return redirect('index')
        else:
            print("kullanıcı adı veya şifre hatalı")
            return redirect('login')
    return render(request,'login.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yapıldı')
    return redirect('index')


