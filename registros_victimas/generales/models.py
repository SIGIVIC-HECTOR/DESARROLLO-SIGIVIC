from django.db import models


class TipoDocumento(models.Model): 
    nombre = models.CharField(max_length=30, unique=True) 
    abreviacion = models.CharField(max_length=10, unique=True)

    class Meta: 
        verbose_name_plural = "Tipos de documentos"

    def __unicode__(self): 
        return self.nombre

class LugarDeclaracion(models.Model):
    departamento_declaracion = models.CharField(max_length=30)
    municipio_declaracion = models.CharField(max_length=50)

    class Meta: 
        verbose_name_plural = "Lugares de declaracion"

    def __unicode__(self): 
        return self.municipio_declaracion


class EntidadAtencion(models.Model):
    nombre_entidad = models.CharField(max_length=30)

    class Meta: 
        verbose_name_plural = "Entidades de atencion"

    def __unicode__(self): 
        return self.nombre_entidad


class EstadoCivil(models.Model):
    tipo_estado_civil = models.CharField(max_length=20)

    class Meta: 
        verbose_name_plural = "Estados civiles"

    def __unicode__(self): 
        return self.tipo_estado_civil


class Genero(models.Model):
    tipo_genero = models.CharField(max_length=20)

    class Meta: 
        verbose_name_plural = "generos"

    def __unicode__(self): 
        return self.tipo_genero


class HechoVictimizario(models.Model):
    tipo_hecho = models.IntegerField()
    descripcion_hecho = models.CharField(max_length=100, blank=True, null=True)

    class Meta: 
        verbose_name_plural = "Hechos victimizarios"

    def __unicode__(self): 
        return self.descripcion_hecho


class PreferenciaEtnica(models.Model):
    nombre_etnia = models.CharField(max_length=50)

    class Meta: 
        verbose_name_plural = "Preferencias etnicas"

    def __unicode__(self): 
        return self.nombre_etnia


class Discapacidad(models.Model):
    tipo_discapacidad = models.CharField(max_length=100)

    class Meta: 
        verbose_name_plural = "Discapacidades"

    def __unicode__(self): 
        return self.tipo_discapacidad


class RegimenEspecial(models.Model):
    tipo_regimen_especial = models.CharField(max_length=20)

    class Meta: 
        verbose_name_plural = "Regimenes especiales"

    def __unicode__(self): 
        return self.tipo_regimen_especial


class Parentezco(models.Model):
    tipo_parentezco = models.CharField(max_length=20)

    class Meta: 
        verbose_name_plural = "Parentezcos"

    def __unicode__(self): 
        return self.tipo_parentezco
