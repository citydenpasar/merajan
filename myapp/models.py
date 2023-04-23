from django.db import models

class Komentar(models.Model):
    nama = models.CharField(max_length=100)
    isi_komentar = models.TextField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='balasan')

    def __str__(self):
        return self.nama

class Betara(models.Model):
    nomor = models.IntegerField()
    nama = models.CharField(max_length=255)
    jenis = models.CharField(max_length=255)
    image = models.CharField(max_length=10000, default="https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png")
    penjelasan = models.TextField()
    
    def __str__(self):
        return self.nama