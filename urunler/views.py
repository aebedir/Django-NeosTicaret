from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    search=''
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(isim__icontains = search)
    context ={
        'urunler':urunler,
        'search':search
    }
    return render(request,'index.html',context)

def detail(request,urunId):
    urunler = Urun.objects.get(id=urunId)
    context={
        'urunum':urunler
    }
    return render(request,'detail.html',context)

def olustur(request):
    if request.method == 'POST':
        resim = request.FILES['resim']
        isim = request.POST['isim']
        aciklama = request.POST['aciklama']
        fiyat = request.POST['fiyat']

        urun = Urun.objects.create(
            isim=isim,
            aciklama=aciklama,
            fiyat=fiyat,
            resim=resim
        )
        urun.save()
        messages.success(request, 'Ürün Başarıyla Eklendi')
        return redirect('olustur')

    return render(request,'olustur.html')