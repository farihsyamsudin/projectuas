from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

def BeritaView(request):
    if request.GET:
        keyword = request.GET["search"]
        data = {
            "title" : "Berita Terkini",
            'beritas' : Berita.objects.filter(judul__contains=keyword),
            'keyword' : keyword
        }
        return render(request, 'berita.html', data)
    else:
        kategorikkp = Kategori.objects.get(kategori = "Berita KKP")
        beritakkp = Berita.objects.filter(kategori_id__kategori = "Berita KKP").order_by('-id')[:6]
        kategorippn = Kategori.objects.get(kategori = "Berita Seputar PPN Karangantu")
        beritappn = Berita.objects.filter(kategori_id__kategori = "Berita Seputar PPN Karangantu").order_by('-id')[:6]
        kategoriumum = Kategori.objects.get(kategori = "Berita Umum Kelautan dan Perikanan")
        beritaumum = Berita.objects.filter(kategori_id__kategori = "Berita Umum Kelautan dan Perikanan").order_by('-id')[:6]
        data = {
            "title" : "Berita Terkini",
            "beritakkps" : beritakkp,
            "kategorikkp" : kategorikkp,
            "beritappns" : beritappn,
            "kategorippn" : kategorippn,
            "beritaumums" : beritaumum,
            "kategoriumum" : kategoriumum,
        }
    return render(request, 'berita.html', data)

def detailBerita(request, pk):
    detail = Berita.objects.get(id = pk)
    data = {
        "title" : 'Detail Berita',
        "detail" : detail
    }
    return render(request, 'detail.html', data)

def beritaCategory(request, cat):
    news = Berita.objects.filter(kategori_id__slug = cat).order_by('-id')
    category = Kategori.objects.get(slug = cat)
    data = {
        "title" : "Kategori",
        "news" : news,
        "cats" : category
    }
    return render(request, 'kategori.html', data) 

@login_required(login_url=settings.LOGIN_URL)
def tambahBerita(request):
    if request.POST:
        form = FormBerita(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['alert'] = "Berhasil menambahkan berita!"
            data = {
                "title" : "Input Data Berita",
                "form" : form,
                "addedNews" : Berita.objects.latest('id')
            }
            return render(request, 'tambahberita.html', data)

    else:
        data = {
            "title" : "Input Data Berita",
            "form" : FormBerita()
        }
    return render(request, 'tambahberita.html', data)

@login_required(login_url=settings.LOGIN_URL)
def editBerita(request, pk):
    beritaedit = Berita.objects.get(id = pk)
    if request.POST:
        if request.FILES:
            beritaedit.cover.delete()
        form = FormBerita(request.POST, request.FILES, instance=beritaedit)
        if form.is_valid():
            form.save()
            request.session['alert'] = "Berhasil mengubah berita!"
            data = {
                "title" : "Edit Berita",
                "form" : FormBerita(),
                "beritaEdit" : beritaedit
            }
            return render(request, 'editberita.html', data)
    else:     
        data = {
            "title" : "Edit Berita",
            "form" : FormBerita(instance=beritaedit),
            "beritaEdit" : beritaedit
        }
    return render(request, 'editberita.html', data)

@login_required(login_url=settings.LOGIN_URL)
def hapusBerita(request, pk):
    berita = Berita.objects.get(id=pk)
    berita.cover.delete()
    berita.delete()
    request.session['alert'] = "Berhasil menghapus berita!"

    return redirect("/berita/")