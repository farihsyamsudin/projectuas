from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Kategori(models.Model):
    kategori = models.CharField(max_length=255, unique=True)
    keterangan = models.TextField()
    slug = models.SlugField(null = True, unique=True, editable=False)

    def save(self):
        self.slug = slugify(self.kategori)
        super().save()

    def __str__(self) -> str:
        return self.kategori

class Berita(models.Model):
    judul = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    isi = RichTextField(blank=True, null=True)
    # isi = models.TextField()
    cover = models.ImageField(upload_to='cover/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    kategori_id = models.ForeignKey(Kategori, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.judul + ' | ' + str(self.author)

    # def get_absolute_url(self):
    #     return reverse("detail", args=(str(self.id)))

