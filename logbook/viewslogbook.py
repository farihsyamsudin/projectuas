from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from .forms import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from logbook.resource import *

# Create your views here.
def datalogbook(request):
    data = {
        "title" : "Data Logbook PPN Karangantu",
        "dataikans" : HasilTangkap.objects.all()
    }
    return render(request, 'data.html', data)

def dataKapal(request):
    data={
        'title' : "Data Kapal",
        'datakapals' : Kapal.objects.all()
    }
    return render(request, 'crudkapal/datakapal.html', data)

def APIDocs(request):
    data = {
        'title' : "Logbook API Docs",
    }
    return render(request, 'docsapi.html', data)




# CRUD KAPAL START

@login_required(login_url=settings.LOGIN_URL)
def createKapal(request):
    if request.POST:
        form = FormKapal(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['alert'] = "Data Kapal Berhasil Ditambahkan"
            data={
                'title' : "Input Data Kapal", 
                'forms' : form,
                'pesan' : "Data berhasil ditambahkan",
            }
            return render(request, 'crudkapal/inputkapal.html', data)
    else:
        data = {
            'title' : "Input Data Kapal",
            'forms' : FormKapal()
        }
    return render(request, 'crudkapal/inputkapal.html', data)

@login_required(login_url=settings.LOGIN_URL)
def updateKapal(request, id):
    kapal = Kapal.objects.get(id = id)
    if request.POST :
        form = FormKapal(request.POST, request.FILES, instance=kapal,)
        if form.is_valid():
            request.session['alert'] = "Data Kapal Berhasil Diubah"
            form.save()
            data = {
                'title' : 'Edit Data Kapal',
                'forms' : form,
                'kapal' : kapal,
                'pesan' : "Data berhasil di ubah"
            }
            return render(request, 'crudkapal/editkapal.html', data)
    else:
        data = {
            'title' : 'Edit Data Kapal',
            'forms' : FormKapal(instance=kapal),
            'kapal' : kapal,
        }
    return render(request, 'crudkapal/editkapal.html', data)

@login_required(login_url=settings.LOGIN_URL)
def deleteKapal(request, id):
    Kapal.objects.get(id=id).delete()
    request.session['alert'] = "Data Kapal Berhasil Dihapus"
    return redirect("/data/kapal/")

# CRUDKAPAL END


# CRUDHASILTANGKAP START

@login_required(login_url=settings.LOGIN_URL)
def crateHasilTangkap(request):
    if request.POST:
        form = FormHasilTangkap(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['alert'] = "Data tangkapan berhasil disimpan"
            data={
                'title' : "Input Data Hasil Tangkap", 
                'forms' : form,
                'pesan' : "Data berhasil ditambahkan",
            }
            return render(request, 'crudhasiltangkap/inputhasilkapal.html', data)
    else:
        data = {
            'title' : "Input Data Hasil Tangkap", 
            'forms' : FormHasilTangkap()
        }
    return render(request, 'crudhasiltangkap/inputhasilkapal.html', data)

@login_required(login_url=settings.LOGIN_URL)
def updateHasilTangkap(request, id):
    hasiltangkap = HasilTangkap.objects.get(id = id)
    if request.POST :
        form = FormHasilTangkap(request.POST, request.FILES, instance=hasiltangkap,)
        if form.is_valid():
            form.save()
            request.session['alert'] = "Data tangkapan berhasil diubah"
            data = {
                'Title' : 'Edit data gempa',
                'forms' : form,
                'hasiltangkap' : hasiltangkap,
                'pesan' : "Data berhasil di ubah"
            }
            return render(request, 'crudhasiltangkap/edithasiltangkap.html', data)
    else:
        data = {
            'Title' : 'Edit data gempa',
            'forms' : FormHasilTangkap(instance=hasiltangkap),
            'hasiltangkap' : hasiltangkap,
        }
    return render(request, 'crudhasiltangkap/edithasiltangkap.html', data)

@login_required(login_url=settings.LOGIN_URL)
def deleteHasilTangkap(request, id):
    HasilTangkap.objects.get(id=id).delete()
    request.session['alert'] = "Data tangkapan berhasil dihapus"
    return redirect("/data/hasiltangkap/")

# CRUDHASILTANGKAP END


# EXPORT DATA START

def export_xls_hasiltangkap(request):
    hasiltangkap = HasilTangkapResources()
    dataset = hasiltangkap.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename = HasilTangkapanPPNKarangantu.xls'
    return response

def export_xls_kapal(request):
    kapal = KapalResources()
    dataset = kapal.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename = KapalPPNKarangantu.xls'
    return response

# EXPORT DATA END


# Grafik Start

def grafikHasilTangkap(request):
    if request.GET :
        bulan = int(request.GET["bulan"])
        tahun = int(request.GET["tahun"])
        datahasiltangkapan = HasilTangkap.objects.filter(tanggal_datang__year=tahun, tanggal_datang__month=bulan)
        data_json = serializers.serialize('json', datahasiltangkapan)
        data = {
            'title' : "Grafik Hasil Tangkapan PPN Karangantu",
            'datahasiltangkap_json' : data_json,
        }
        return render(request, 'grafik.html', data)

    else :
        datahasiltangkapan = HasilTangkap.objects.all()
        data_json = serializers.serialize('json', datahasiltangkapan)
        data = {
            'title' : "Grafik Hasil Tangkapan PPN Karangantu",
            'datahasiltangkap_json' : data_json,
        }
    return render(request, 'grafik.html', data)

# Grafik End