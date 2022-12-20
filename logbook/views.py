from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from news.models import *
from .forms import *

# Create your views here.

# Create your views here.
def index(request):
    beritaTerkini = Berita.objects.all().order_by('-id')[:5]
    data = {
        'title' : "Web",
        'beritaTerkini' : beritaTerkini,
        'petas' : Peta.objects.all()
    }
    return render(request, 'index.html', data)

def Signup(request):
    if request.POST:
        form = FormAdminRequst(request.POST)
        if form.is_valid():
            form.save()
            request.session['alert'] = "Permintaan Signup diterima, anda akan dihubungi melalui email jika akun anda sudah aktif"
            data={
                'title' : "Input Data Kapal", 
                'forms' : form,
            }
            return redirect('/')
    else:
        data = {
            'title' : "Signup Admin",
            "form" : FormAdminRequst()
        }
    return render(request, 'registration/signup.html', data)

@login_required(login_url=settings.LOGIN_URL)
def AdminPage(request):
    data = {
        'title' : 'Halaman Admin',
        'pesans' : PesanKontak.objects.all(),
        'petas' : Peta.objects.all(),
        'beritas' : Berita.objects.all()
    }
    return render(request, 'admin.html', data)

@login_required(login_url=settings.LOGIN_URL)
def SimpanPesan(request):
    if request.POST :
        form = FormPesan(request.POST)
        if form.is_valid():
            form.save()
            request.session['alert'] = "Berhasil mengirim psan ke admin!. Harap jangan Spam ya!"
            return redirect('/')
    else:
        return redirect('/')

@login_required(login_url=settings.LOGIN_URL)
def HapusPesan(request, id):
    PesanKontak.objects.get(id=id).delete()
    request.session['alert'] = "Pesan Berhasil Dihapus"
    return redirect("/adminpage/")

@login_required(login_url=settings.LOGIN_URL)
def SimpanPeta(request):
    if request.POST :
        request.session['alert'] = "Data Berhasil Disimpan"
        form = FormPeta(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/adminpage/')
    else:
        request.session['alert'] = "Gagal menyimpan peta"
        return redirect('/adminpage/')

@login_required(login_url=settings.LOGIN_URL)
def EditPeta(request):
    if request.POST:
        petaedit = Peta.objects.get(id = request.POST['id'])
        if request.FILES:
            petaedit.folder.delete()
        form = FormPeta(request.POST, request.FILES, instance=petaedit)
        if form.is_valid():
            request.session['alert'] = "Data Berhasil Diubah"
            form.save()
            return redirect('/adminpage/')
    return redirect('/adminpage/')

@login_required(login_url=settings.LOGIN_URL)
def HapusPeta(request, id):
    request.session['alert'] = "Data Berhasil Dihapus"
    peta = Peta.objects.get(id=id)
    peta.folder.delete()
    peta.delete()
    return redirect("/adminpage/")

def unset_session(request):
    if 'alert' in request.session:
        del request.session['alert']
    return redirect(request.path)