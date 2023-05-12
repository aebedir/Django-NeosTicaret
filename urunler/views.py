from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    search=''
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
        Q(isim__icontains = search)|
        Q(kategori__isim__icontains = search)
        )
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
    kategoriler = Kategori.objects.all()
    if request.method == 'POST':
        resim = request.FILES['resim']
        isim = request.POST['isim']
        aciklama = request.POST['aciklama']
        fiyat = request.POST['fiyat']
        kategori = request.POST['kategori']

        urun = Urun.objects.create(
            kategori_id=kategori,
            isim=isim,
            aciklama=aciklama,
            fiyat=fiyat,
            resim=resim
        )
        urun.save()
        messages.success(request, 'Ürün Başarıyla Eklendi')
        return redirect('olustur')
    context = {
        'kategoriler':kategoriler
    }

    return render(request,'olustur.html',context)