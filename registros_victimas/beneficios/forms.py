# -*- coding: 850 -*-
from django import forms
from beneficios.models import *
from generales.models import *


"""Las clases form estructuran el formulario que se presentará al usuario a partir de la entidad de la base de datos que se requiera instanciar,
se construye la clase meta donde se tiene el model (modelo o entidad de la base de datos), fields(los campos de la entidad de la bd que serán 
llamados), labels(los campos llamados y sus respectivas etiquetas a presentar al usuario) y widgets(los campos llamados y el tipo de componente
que será usado para diligenciar cada campo como tipo campo de texto, cuadro de texto, numérico, email, desplegable, etc.)"""

class beneficioVictimaForm(forms.ModelForm):

    class Meta:
        model = BeneficioVictima
        fields = [
            'derecho',
            'condiciones_problematica',
            'nombre_programa',
            'estado_gestion_programa',
            'meta_programa',
            'avance_meta_programa',
            'indicadores',
            'coofinanciacion_nacional',
            'fosyga_etesa',
            'otros_recursos_nacionales',
            'coofinanciacion_departamental',
            'otros_recursos_departamentales',
            'recursos_propios',
            'sistema_general_participacion',
            'regalia',
            'credito',
            'otros_recursos_municipales',
            'empresa_privada',
            'cooperacion_otros',
            'otros',
            'participacion_nacional',
            'participacion_departamental',
            'participacion_municipal',
            'cooperacion_internacional',
            'participacion_otros',
        ]
        labels = {
            'derecho': 'Derecho (*)',
            'condiciones_problematica': 'Condiciones de la problemática (*)',
            'nombre_programa': 'Nombre del programa (*)',
            'estado_gestion_programa': 'Estado de la gestión del programa (*)',
            'meta_programa': 'Meta del programa (*)',
            'avance_meta_programa': 'Avance de la meta del programa',
            'indicadores': 'Indicadores',
            'coofinanciacion_nacional': 'Coofinanciación nacional',
            'fosyga_etesa': 'FOSYGA y ETESA',
            'otros_recursos_nacionales': 'Otros recursos nacionales',
            'coofinanciacion_departamental': 'Coofinanciación departamental',
            'otros_recursos_departamentales': 'Otros recursos departamentales',
            'recursos_propios': 'Recursos propios',
            'sistema_general_participacion': 'Sistema general de participación',
            'regalia': 'Regalía',
            'credito': 'Crédito',
            'otros_recursos_municipales': 'Otros recursos municipales',
            'empresa_privada': 'Empresa privada',
            'cooperacion_otros': 'Cooperación de otros',
            'otros': 'Otros',
            'participacion_nacional': 'Participación nacional',
            'participacion_departamental': 'Participación departamental',
            'participacion_municipal': 'Participación municipal',
            'cooperacion_internacional': 'Cooperación internacional',
            'participacion_otros': 'Participación de otros',
        }
        widgets = {
            'derecho': forms.Select(attrs={'class': 'form-control'}),
            'condiciones_problematica': forms.Textarea(attrs={'class': 'form-control'}),
            'nombre_programa': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_gestion_programa': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_programa': forms.Textarea(attrs={'class': 'form-control'}),
            'avance_meta_programa': forms.NumberInput(attrs={'class': 'form-control'}),
            'indicadores': forms.NumberInput(attrs={'class': 'form-control'}),
            'coofinanciacion_nacional': forms.NumberInput(attrs={'class': 'form-control'}),
            'fosyga_etesa': forms.NumberInput(attrs={'class': 'form-control'}),
            'otros_recursos_nacionales': forms.NumberInput(attrs={'class': 'form-control'}),
            'coofinanciacion_departamental': forms.NumberInput(attrs={'class': 'form-control'}),
            'otros_recursos_departamentales': forms.NumberInput(attrs={'class': 'form-control'}),
            'recursos_propios': forms.NumberInput(attrs={'class': 'form-control'}),
            'sistema_general_participacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'regalia': forms.NumberInput(attrs={'class': 'form-control'}),
            'credito': forms.NumberInput(attrs={'class': 'form-control'}),
            'otros_recursos_municipales': forms.NumberInput(attrs={'class': 'form-control'}),
            'empresa_privada': forms.NumberInput(attrs={'class': 'form-control'}),
            'cooperacion_otros': forms.NumberInput(attrs={'class': 'form-control'}),
            'otros': forms.NumberInput(attrs={'class': 'form-control'}),
            'participacion_nacional': forms.Textarea(attrs={'class': 'form-control'}),
            'participacion_departamental': forms.Textarea(attrs={'class': 'form-control'}),
            'participacion_municipal': forms.Textarea(attrs={'class': 'form-control'}),
            'cooperacion_internacional': forms.Textarea(attrs={'class': 'form-control'}),
            'participacion_otros': forms.Textarea(attrs={'class': 'form-control'}),
        }