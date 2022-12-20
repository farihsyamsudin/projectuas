from .models import *
from .serializers import *
from rest_framework import viewsets

class HasilTangkapViewset(viewsets.ModelViewSet):
    queryset = HasilTangkap.objects.all()
    serializer_class = HasilTangkapanSerializer
    http_method_names = ['get']

class KapalViewset(viewsets.ModelViewSet):
    queryset = Kapal.objects.all()
    serializer_class = KapalSerializer
    http_method_names = ['get']