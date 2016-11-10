# -*- coding: 850 -*-
from django import forms
from django.forms import ModelForm
from solicitantes.models import *
from generales.models import *
import datetime
import django.core.validators
from django.conf.global_settings import SHORT_DATE_FORMAT

"""Las clases form estructuran el formulario que se presentará al usuario a partir de la entidad de la base de datos que se requiera instanciar,
se construye la clase meta donde se tiene el model (modelo o entidad de la base de datos), fields(los campos de la entidad de la bd que serán 
llamados), labels(los campos llamados y sus respectivas etiquetas a presentar al usuario) y widgets(los campos llamados y el tipo de componente
que será usado para diligenciar cada campo como tipo campo de texto, cuadro de texto, numérico, email, desplegable, etc.)"""


class addInformacionSolicitanteForm(forms.ModelForm):#formulario para el cliente

    class Meta:
        model = InformacionSolicitante
        fields = [
            'tipo_documento',
            'nombre',
            'direccion',
            'celular',
            'telefono',
            'email',
            'descripcion',
        ]
        labels = {
            'tipo_documento': 'Tipo de documento (*)',
            'nombre': 'Nombre completo (*)',
            'direccion': 'Dirección (*)',
            'celular': 'Celular',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico (*)',
            'descripcion': 'Descripción de los hechos (*)',
        }
        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }


class informacionSolicitanteForm(forms.ModelForm):#formulario para el administrador

    class Meta:
        ESTADO = (('Atendido', 'Atendido'), ('En revision', 'En revision'), ('Pendiente', 'Pendiente'))
        model = InformacionSolicitante
        fields = [
            'declaracion',
            'tipo_documento',
            'nombre',
            'direccion',
            'celular',
            'telefono',
            'email',
            'descripcion',
            'estado_revision',
        ]
        labels = {
            'declaracion': 'Declaracion relacionada',
            'tipo_documento': 'Tipo de documento (*)',
            'nombre': 'Nombre completo (*)',
            'direccion': 'Dirección (*)',
            'celular': 'Celular',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico (*)',
            'descripcion': 'Descripción de los hechos (*)',
            'estado_revision': 'Estado (*)',
        }
        widgets = {
            'declaracion': forms.Select(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado_revision': forms.Select(attrs={'class': 'form-control'}, choices=ESTADO),
        }


class asociadoForm(forms.ModelForm):

    class Meta:
        SN = (('SI', 'SI'), ('NO', 'NO'))
        model = AsociadoDeclarante
        fields = [
            'declaracion',
            'parentezco',
            'estado_civil',
            'regimen_especial',
            'genero',
            'tipo_documento',
            'primer_nombre_asociado',
            'demas_nombres_asociado',
            'primer_apellido_asociado',
            'segundo_apellido_asociado',
            'numero_documento_asociado',
            'fecha_nacimiento_asociado',
            'mujer_cabeza_familia',
            'gestante_lactante',
            'estado_atencion_asociado',
        ]
        labels = {
            'declaracion': 'Id declaracion',
            'parentezco': 'Parentezco',
            'estado_civil': 'Estado civil',
            'regimen_especial': 'Regimen especial',
            'genero': 'Genero',
            'tipo_documento': 'Tipo de documento',
            'primer_nombre_asociado': 'Primer nombre',
            'demas_nombres_asociado': 'Demás nombres',
            'primer_apellido_asociado': 'Primer apellido',
            'segundo_apellido_asociado': 'Segundo apellido',
            'numero_documento_asociado': 'Número de documento',
            'fecha_nacimiento_asociado': 'Fecha de nacimiento',
            'mujer_cabeza_familia': 'Mujer cabeza de hogar',
            'gestante_lactante': 'Gestante o lactante',
            'estado_atencion_asociado': 'Estado de atención',
        }
        widgets = {
            'declaracion': forms.Select(attrs={'class': 'form-control'}),
            'parentezco': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'regimen_especial': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'primer_nombre_asociado': forms.TextInput(attrs={'class': 'form-control'}),
            'demas_nombres_asociado': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_apellido_asociado': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido_asociado': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento_asociado': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento_asociado': forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'myDateClass', 'placeholder':'ej. 21-01-1990'}),
            'mujer_cabeza_familia': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'gestante_lactante': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'estado_atencion_asociado': forms.TextInput(attrs={'class': 'form-control'}),
        }


class beneficioAsociadoForm(forms.ModelForm):

    class Meta:
        ESTADO = (('Atendido', 'Atendido'), ('Pendiente', 'Pendiente'))
        model = BeneficioAsociado
        fields = [
            'beneficio',
            'estado_actual_beneficio',
        ]
        labels = {
            'beneficio': 'Beneficio (*)',
            'estado_actual_beneficio': 'Estado actual (*)',
        }
        widgets = {
            'beneficio': forms.Select(attrs={'class': 'form-control'}),
            'estado_actual_beneficio': forms.Select(attrs={'class': 'form-control'}, choices=ESTADO),
        }


class correccionDeclaracionForm(forms.ModelForm):

    class Meta:
        model = CorreccionDeclaracion
        fields = [
            'declaracion',
            'descripcion_correccion',
        ]
        labels = {
            'declaracion': 'Id declaracion (*)',
            'descripcion_correccion': 'Descripcion (*)',
        }
        widgets = {
            'declaracion': forms.Select(attrs={'class': 'form-control'}),
            'descripcion_correccion': forms.Textarea(attrs={'class': 'form-control'}),
        }


class tipoIntermediarioForm(forms.ModelForm):

    class Meta:
        model = TipoIntermediario
        fields = [
            'tipo_intermediario',
            'institucion_perteneciente',
        ]
        labels = {
            'tipo_intermediario': 'Tipo de intermediario (*)',
            'institucion_perteneciente': 'Institución a la que pertenece (*)',
        }
        widgets = {
            'tipo_intermediario': forms.TextInput(attrs={'class': 'form-control'}),
            'institucion_perteneciente': forms.TextInput(attrs={'class': 'form-control'}),
        }


class declaracionForm(forms.ModelForm):

    class Meta:
        SN = (('SI', 'SI'), ('NO', 'NO'))
        model = TomaDeclaracion
        fields = [
            'codigo_declaracion',
            'lugar_declaracion',
            'entidad',
            'tipo_documento',
            'numero_documento_declarante',
            'descripcion_hecho',
            'fecha_declaracion',
            'primer_nombre_declarante',
            'demas_nombres_declarante',
            'primer_apellido_declarante',
            'segundo_apellido_declarante',
            'fecha_nacimiento_declarante',
            'direccion_declarante',
            'barrio_declarante',
            'vereda_declarante',
            'departamento_declarante',
            'municipio_declarante',
            'email_declarante',
            'fijo_declarante',
            'celular_declarante',
            'direccion_alt_declarante',
            'barrio_alt_declarante',
            'vereda_alt_declarante',
            'departamento_alt_declarante',
            'municipio_alt_declarante',
            'email_alt_declarante',
            'fijo_alt_declarante',
            'celular_alt_declarante',
            'autorizacion_declarante',
            'mensajes_celular_declarante',
            'mensajes_fijo_declarante',
            'mensajes_email_declarante',
            'mensajes_otros_declarante',
            'estado_atencion_declarador',
        ]
        labels = {
            'codigo_declaracion':'Código de la declaración (*)',
            'lugar_declaracion': 'Lugar de declaración (*)',
            'entidad': 'Entidad de atención',
            'tipo_documento': 'Tipo de documento (*)',
            'numero_documento_declarante': 'Número de documento',
            'descripcion_hecho': 'Descripción de los hechos (*)',
            'fecha_declaracion': 'Fecha de la declaración (*)',
            'primer_nombre_declarante': 'Primer nombre (*)',
            'demas_nombres_declarante': 'Demás nombres',
            'primer_apellido_declarante': 'Primer apellido (*)',
            'segundo_apellido_declarante': 'Segundo apellido',
            'fecha_nacimiento_declarante': 'Fecha de nacimiento',
            'direccion_declarante': 'Dirección (*)',
            'barrio_declarante': 'Barrio',
            'vereda_declarante': 'Vereda',
            'departamento_declarante': 'Departamento (*)',
            'municipio_declarante': 'Municipio (*)',
            'email_declarante': 'Correo electrónico',
            'fijo_declarante': 'Teléfono fijo',
            'celular_declarante': 'Número de celular',
            'direccion_alt_declarante': 'Dirección alternativa',
            'barrio_alt_declarante': 'Barrio alternativo',
            'vereda_alt_declarante': 'Vereda alternativa',
            'departamento_alt_declarante': 'Departamento alternativo',
            'municipio_alt_declarante': 'Municipio alternativo',
            'email_alt_declarante': 'Correo electrónico alternativo',
            'fijo_alt_declarante': 'Teléfono fijo alternativo',
            'celular_alt_declarante': 'Número celular alternativo',
            'autorizacion_declarante': 'Autoriza el declarante',
            'mensajes_celular_declarante': 'Enviar mensajes al celular',
            'mensajes_fijo_declarante': 'Enviar mensajes al fijo',
            'mensajes_email_declarante': 'Enviar mensajes al correo electrónico',
            'mensajes_otros_declarante': 'Enviar mensajes a otros',
            'estado_atencion_declarador': 'Estado de atención del declarador (*)',
        }
        widgets = {
            'codigo_declaracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'lugar_declaracion': forms.Select(attrs={'class': 'form-control'}),
            'entidad': forms.Select(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'numero_documento_declarante': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion_hecho': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha_declaracion': forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'myDateClass', 'placeholder':'ej. 21-01-2016'}),
            'primer_nombre_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'demas_nombres_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_apellido_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento_declarante': forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'myDateClass', 'placeholder':'ej. 21-01-1990'}),
            'direccion_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'barrio_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'vereda_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'email_declarante': forms.EmailInput(attrs={'class': 'form-control'}),
            'fijo_declarante': forms.NumberInput(attrs={'class': 'form-control'}),
            'celular_declarante': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion_alt_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'barrio_alt_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'vereda_alt_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento_alt_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio_alt_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'email_alt_declarante': forms.EmailInput(attrs={'class': 'form-control'}),
            'fijo_alt_declarante': forms.NumberInput(attrs={'class': 'form-control'}),
            'celular_alt_declarante': forms.NumberInput(attrs={'class': 'form-control'}),
            'autorizacion_declarante': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'mensajes_celular_declarante': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'mensajes_fijo_declarante': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'mensajes_email_declarante': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'mensajes_otros_declarante': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_atencion_declarador': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

        

class declaranteAsociadoForm(forms.ModelForm):

    class Meta:
        SN = (('SI', 'SI'), ('NO', 'NO'))
        model = AsociadoDeclarante
        fields = [
            'estado_civil',
            'regimen_especial',
            'genero',
            'mujer_cabeza_familia',
            'gestante_lactante',
        ]
        labels = {
            'estado_civil': 'Estado civil',
            'regimen_especial': 'Regimen especial',
            'genero': 'Genero',
            'mujer_cabeza_familia': 'Mujer cabeza de hogar',
            'gestante_lactante': 'Gestante o lactante',
        }
        widgets = {
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'regimen_especial': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'mujer_cabeza_familia': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'gestante_lactante': forms.Select(attrs={'class': 'form-control'}, choices=SN),
        }


class discapacidadAsociadoForm(forms.ModelForm):

    class Meta:
        model = DiscapacidadAsociado
        fields = [
            'discapacidad',
        ]
        labels = {
            'discapacidad': 'Discapacidad (*)',
        }
        widgets = {
            'discapacidad': forms.Select(attrs={'class': 'form-control'}),
        }


class etniaAsociadoForm(forms.ModelForm):

    class Meta:
        model = EtniaAsociado
        fields = [
            'etnia',
        ]
        labels = {
            'etnia': 'Etnia (*)',
        }
        widgets = {
            'etnia': forms.Select(attrs={'class': 'form-control'}),
        }


class intermediarioForm(forms.ModelForm):

    class Meta:
        SN = (('SI', 'SI'), ('NO', 'NO'))
        model = Intermediario
        fields = [
            'tipo_documento',
            'tipo_intermediario',
            'declaracion',
            'primer_nombre_intermediario',
            'demas_nombres_intermediario',
            'primer_apellido_intermediario',
            'segundo_apellido_intermediario',
            'numero_documento_intermediario',
            'direccion_intermediario',
            'telefono_intermediario',
        ]
        labels = {
            'tipo_documento': 'Tipo de documento (*)',
            'tipo_intermediario': 'Tipo de intermediario (*)',
            'declaracion': 'Declaración',
            'primer_nombre_intermediario': 'Primer nombre (*)',
            'demas_nombres_intermediario': 'Demás nombres',
            'primer_apellido_intermediario': 'Primer apellido (*)',
            'segundo_apellido_intermediario': 'Segundo apellido',
            'numero_documento_intermediario': 'Número de documento (*)',
            'direccion_intermediario': 'Dirección',
            'telefono_intermediario': 'Número de telefono',
        }
        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'tipo_intermediario': forms.Select(attrs={'class': 'form-control'}),
            'declaracion': forms.Select(attrs={'class': 'form-control'}),
            'primer_nombre_intermediario': forms.TextInput(attrs={'class': 'form-control'}),
            'demas_nombres_intermediario': forms.TextInput(attrs={'class': 'form-control'}),
            'primer_apellido_intermediario': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_apellido_intermediario': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento_intermediario': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion_intermediario': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_intermediario': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class hechoAsociadoForm(forms.ModelForm):

    class Meta:
        model = HechoAsociado
        fields = [
            'hecho',
        ]
        labels = {
            'hecho': 'Id hecho (*)',
        }
        widgets = {
            'hecho': forms.Select(attrs={'class': 'form-control'}),
        }


class hechoDeclaranteForm(forms.ModelForm):

    class Meta:
        model = HechoDeclarante
        fields = [
            'hecho',
            'cantidad_eventos',
        ]
        labels = {
            'hecho': 'Id hecho (*)',
            'cantidad_eventos': 'Cantidad de sucesos (*)',
        }
        widgets = {
            'hecho': forms.Select(attrs={'class': 'form-control'}),
            'cantidad_eventos': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class verificacionProcedimientoForm(forms.ModelForm):

    class Meta:
        SN = (('SI', 'SI'), ('NO', 'NO'))
        model = VerificacionProcedimiento
        fields = [
            'total_anexos_diligenciados',
            'total_soportes_aportados',
            'total_folios_declaracion',
            'realiza_entrevista_previa',
            'declarante_lee_declaracion',
            'declarante_orientado_corregir',
            'correcciones_incluidas',
            'observaciones_funcionario',
            'declarante_sabe_firmar',
        ]
        labels = {
            'total_anexos_diligenciados': 'Total de anexos diligenciados (*)',
            'total_soportes_aportados': 'Total de soportes aportados',
            'total_folios_declaracion': 'Total de folios (*)',
            'realiza_entrevista_previa': 'Realiza la entrevista previa',
            'declarante_lee_declaracion': 'El declarante sabe leer',
            'declarante_orientado_corregir': 'El declarante es orientado a corregir',
            'correcciones_incluidas': 'Correcciones incluidas',
            'observaciones_funcionario': 'Observaciones del funcionario',
            'declarante_sabe_firmar': 'El declarante sabe firmar',
        }
        widgets = {
            'total_anexos_diligenciados': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_soportes_aportados': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_folios_declaracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'realiza_entrevista_previa': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'declarante_lee_declaracion': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'declarante_orientado_corregir': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'correcciones_incluidas': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'observaciones_funcionario': forms.Select(attrs={'class': 'form-control'}, choices=SN),
            'declarante_sabe_firmar': forms.Select(attrs={'class': 'form-control'}, choices=SN),
        }