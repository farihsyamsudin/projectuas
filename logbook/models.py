from django.db import models

# Create your models here.

class AdminRequest(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username

class Peta(models.Model):
    nama_peta = models.TextField(max_length=40)
    folder = models.FileField(upload_to='peta/')
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.nama_peta

class PesanKontak(models.Model):
    email_pesan = models.EmailField()
    name_pesan = models.CharField(max_length=255)
    message = models.TextField()

class Kapal(models.Model):
    nama_kapal = models.CharField(max_length=150)
    pemilik = models.CharField(max_length=150)
    nahkoda = models.CharField(max_length=150)
    sipi = models.CharField(max_length=150)
    masa_berlaku = models.DateField()
    abk_lokal = models.IntegerField()
    abk_asing = models.IntegerField()
    bobot = models.IntegerField()
    panjang = models.FloatField()
    dk = models.FloatField()
    tanda_selar = models.CharField(max_length=150)
    alat_tangkap = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nama_kapal

class HasilTangkap(models.Model):
    kapal_id = models.ForeignKey(Kapal, on_delete=models.CASCADE)
    daerah_penangkapan = models.CharField(max_length=150)
    wpp = models.IntegerField()
    tanggal_berangkat = models.DateField()
    tanggal_datang = models.DateField()
    bondolan = models.IntegerField()
    cumi = models.IntegerField()
    etem = models.IntegerField()
    japuh = models.IntegerField()
    kuniran = models.IntegerField()
    layang = models.IntegerField()
    selar = models.IntegerField()
    tembang = models.IntegerField()
    tongkol = models.IntegerField()
    teri = models.IntegerField()
    tengkek = models.IntegerField()

    def __str__(self) -> str:
        return self.kapal_id.nama_kapal
    

