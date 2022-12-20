from django.shortcuts import render

# Create your views here.
def tidesInfo(request):
    data = {
        'title' : "Informasi Gelombang Pasang",
        'api_key' : '399181ac-4eb9-43b9-acf8-28aa81cbcaaa',
    }
    return render(request, 'tides.html', data)