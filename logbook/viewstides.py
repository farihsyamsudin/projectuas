from django.shortcuts import render

# Create your views here.
def tidesInfo(request):
    data = {
        'title' : "Informasi Gelombang Pasang",
        'api_key' : 'be178de0-dacc-4829-ae26-95b2c5888a63',
    }
    return render(request, 'tides.html', data)