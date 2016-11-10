# -*- coding: 850 -*-
from django import forms
from beneficios.models import *
from generales.models import *

"""Las clases form estructuran el formulario que se presentará al usuario a partir de la entidad de la base de datos que se requiera instanciar,
se construye la clase meta donde se tiene el model (modelo o entidad de la base de datos), fields(los campos de la entidad de la bd que serán 
llamados), labels(los campos llamados y sus respectivas etiquetas a presentar al usuario) y widgets(los campos llamados y el tipo de componente
que será usado para diligenciar cada campo como tipo campo de texto, cuadro de texto, numérico, email, desplegable, etc.)"""

class addTipoDocumentoForm(forms.Form):
	nombre = forms.CharField(max_length=30, help_text='*Campo obligatorio')
	abreviacion = forms.CharField(max_length=10, help_text='*Campo obligatorio')

	def clean(self):
		return self.cleaned_data

class entidadAtencionForm(forms.ModelForm):

    class Meta:
        model = EntidadAtencion
        fields = [
            'nombre_entidad',        ]
        labels = {
            'nombre_entidad': 'Nombre de la entidad (*)',
        }
        widgets = {
            'nombre_entidad': forms.TextInput(attrs={'class': 'form-control'}),
        }


class lugarDeclaracionForm(forms.ModelForm):

    class Meta:
        model = LugarDeclaracion
        fields = [
            'departamento_declaracion',
            'municipio_declaracion',        ]
        labels = {
            'departamento_declaracion': 'Departamento (*)',
            'municipio_declaracion': 'Municipio (*)',
        }
        widgets = {
            'departamento_declaracion': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio_declaracion': forms.TextInput(attrs={'class': 'form-control'}),
        }
