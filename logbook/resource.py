from import_export import resources
from .models import *
from import_export.fields import Field

class HasilTangkapResources(resources.ModelResource):
    kapal_id__nama_kapal = Field(attribute='kapal_id', column_name='Nama Kapal')

    class Meta:
        model = HasilTangkap
        fields = ['kapal_id__nama_kapal', 'daerah_penangkapan', 'wpp', 'tanggal_berangkat', 'tanggal_datang', 'bondolan', 'cumi', 'etem', 'japuh', 'kuniran', 'layang', 'selar', 'tembang', 'tongkol', 'teri', 'tengkek']
        # order_by

class KapalResources(resources.ModelResource):
    class Meta:
        model = Kapal
        fields = "__all__"