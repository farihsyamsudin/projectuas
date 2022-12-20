from django import forms
from django.forms import ModelForm
from .models import *

class FormBerita(ModelForm):
    class Meta:
        model = Berita
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput(attrs={
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
            'author' : forms.Select({
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
            'isi' : forms.Textarea({
                'class' : 'py-2 px-4 rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600 w-full text-sm'
            }),
            'cover' : forms.FileInput({
                'class' : 'py-2 rounded-md focus:outline-none -my-1 my-2 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-200 file:text-violet-700 hover:file:bg-violet-100 text-slate-500'
            }),
            'kategori_id' : forms.Select({
                'class' : 'py-2 px-4 font-ssp rounded-md block mb-4 focus:outline-none focus:ring-2 focus:ring-blue-600 border-2 border-blue-600'
            }),
        }