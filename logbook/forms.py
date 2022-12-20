from django import forms
from django.forms import ModelForm
from .models import *

class FormPesan(ModelForm):
    class Meta:
        model = PesanKontak
        fields = '__all__'

class FormPeta(ModelForm):
    class Meta:
        model = Peta
        fields = '__all__'

class FormAdminRequst(ModelForm):
    class Meta:
        model = AdminRequest
        fields = '__all__'

class FormKapal(ModelForm):
    class Meta:
        model = Kapal
        fields = '__all__'

        widgets = {
            'nama_kapal' : forms.TextInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
            'pemilik' : forms.TextInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
            'nahkoda' : forms.TextInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
            'sipi' : forms.TextInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
            'masa_berlaku' : forms.DateInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'date'
            }),
            'abk_lokal' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'abk_asing' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'bobot' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'panjang' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number', 'step' : '0.001'
            }),
            'dk' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number', 'step' : '0.001'
            }),
            'tanda_selar' : forms.TextInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600',
            }),
            'alat_tangkap' : forms.TextInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600',
            }),
        }

class FormHasilTangkap(ModelForm):
    class Meta:
        model = HasilTangkap
        fields = '__all__'

        widgets = {
            'kapal_id' : forms.Select(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
            'daerah_penangkapan' : forms.TextInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
            'wpp' : forms.TextInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
            'tanggal_datang' : forms.DateInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'date'
            }),
            'tanggal_berangkat' : forms.DateInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'date'
            }),
            'bondolan' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'cumi' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'etem' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'japuh' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'kuniran' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'layang' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'selar' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'tembang' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'tongkol' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'teri' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
            'tengkek' : forms.NumberInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600', 'type' : 'number'
            }),
        }

