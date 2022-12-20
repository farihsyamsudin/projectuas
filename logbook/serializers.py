from .models import *
from rest_framework import serializers

class HasilTangkapanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HasilTangkap()
        fields = ['kapal_id', 'daerah_penangkapan', 'wpp', 'tanggal_berangkat', 'tanggal_datang', 'bondolan', 'cumi', 'etem', 'japuh', 'kuniran', 'layang', 'selar', 'tembang', 'tongkol', 'teri', 'tengkek']
        
class KapalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kapal()
        fields = '__all__'