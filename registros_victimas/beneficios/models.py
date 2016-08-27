from django.db import models


class Derecho(models.Model):
    nombre_componente_politica = models.CharField(max_length=50)
    nombre_derecho = models.CharField(max_length=50)

    class Meta: 
        verbose_name_plural = 'Derechos involucrados'

    def __unicode__(self): 
        return self.nombre_derecho

class BeneficioVictima(models.Model):
    derecho = models.ForeignKey('Derecho')
    condiciones_problematica = models.CharField(max_length=1024)
    nombre_programa = models.CharField(max_length=100)
    estado_gestion_programa = models.CharField(max_length=50)
    meta_programa = models.CharField(max_length=1024)
    avance_meta_programa = models.BigIntegerField(blank=True, null=True)
    indicadores = models.BigIntegerField(blank=True, null=True)
    coofinanciacion_nacional = models.BigIntegerField(blank=True, null=True)
    fosyga_etesa = models.BigIntegerField(blank=True, null=True)
    otros_recursos_nacionales = models.BigIntegerField(blank=True, null=True)
    coofinanciacion_departamental = models.BigIntegerField(blank=True, null=True)
    otros_recursos_departamentales = models.BigIntegerField(blank=True, null=True)
    recursos_propios = models.BigIntegerField(blank=True, null=True)
    sistema_general_participacion = models.BigIntegerField(blank=True, null=True)
    regalia = models.BigIntegerField(blank=True, null=True)
    credito = models.BigIntegerField(blank=True, null=True)
    otros_recursos_municipales = models.BigIntegerField(blank=True, null=True)
    empresa_privada = models.BigIntegerField(blank=True, null=True)
    cooperacion_otros = models.BigIntegerField(blank=True, null=True)
    otros = models.BigIntegerField(blank=True, null=True)
    participacion_nacional = models.CharField(max_length=1024, blank=True, null=True)
    participacion_departamental = models.CharField(max_length=1024, blank=True, null=True)
    participacion_municipal = models.CharField(max_length=1024, blank=True, null=True)
    cooperacion_internacional = models.CharField(max_length=1024, blank=True, null=True)
    participacion_otros = models.CharField(max_length=1024, blank=True, null=True)

    class Meta: 
        verbose_name_plural = 'Beneficios'

    def __unicode__(self): 
        return self.nombre_programa


