from django.db import models

# Create your models here.

class Urun(models.Model):
    isim = models.CharField(max_length=100)
    aciklama = models.TextField(max_length=500)
    resim = models.FileField(upload_to = 'urunler/', null = True)
    fiyat = models.IntegerField()

    def __str__(self):
        return self.isim
    

#database relationship




