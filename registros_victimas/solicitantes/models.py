from django.db import models

class AsociadoDeclarante(models.Model):
    declaracion = models.ForeignKey('TomaDeclaracion')
    parentezco = models.ForeignKey('generales.Parentezco', blank=True, null=True)
    estado_civil = models.ForeignKey('generales.EstadoCivil', blank=True, null=True)
    regimen_especial = models.ForeignKey('generales.RegimenEspecial', blank=True, null=True)
    genero = models.ForeignKey('generales.Genero', blank=True, null=True)
    tipo_documento = models.ForeignKey('generales.TipoDocumento')
    primer_nombre_asociado = models.CharField(max_length=20)
    demas_nombres_asociado = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido_asociado = models.CharField(max_length=20)
    segundo_apellido_asociado = models.CharField(max_length=20, blank=True, null=True)
    numero_documento_asociado = models.BigIntegerField()
    fecha_nacimiento_asociado = models.CharField(max_length=20)
    mujer_cabeza_familia = models.CharField(max_length=2)
    gestante_lactante = models.CharField(max_length=2)
    estado_atencion_asociado = models.CharField(max_length=15)

    class Meta: 
        verbose_name_plural = 'Asociados del declarante'

    def __unicode__(self): 
        return '%s %s %s (%s)' % (self.primer_nombre_asociado, self.primer_apellido_asociado,
            self.segundo_apellido_asociado, self.numero_documento_asociado)


class BeneficioAsociado(models.Model):
    asociado = models.ForeignKey('AsociadoDeclarante')
    beneficio = models.ForeignKey('beneficios.BeneficioVictima')
    estado_actual_beneficio = models.CharField(max_length=30)

    class Meta: 
        verbose_name_plural = 'Beneficios obtenidos'

    def __unicode__(self): 
        return self.estado_actual_beneficio


class CorreccionDeclaracion(models.Model):
    declaracion = models.ForeignKey('TomaDeclaracion')
    descripcion_correccion = models.CharField(max_length=1024)

    class Meta: 
        verbose_name_plural = 'Correcciones de las declaraciones'

    def __unicode__(self): 
        return self.declaracion


class DiscapacidadAsociado(models.Model):
    discapacidad = models.ForeignKey('generales.Discapacidad')
    asociado = models.ForeignKey('AsociadoDeclarante')

    class Meta: 
        verbose_name_plural = 'Discapacidades de cada asociado'

    def __unicode__(self): 
        return self.discapacidad


class EtniaAsociado(models.Model):
    etnia = models.ForeignKey('generales.PreferenciaEtnica')
    asociado = models.ForeignKey('AsociadoDeclarante')

    class Meta: 
        verbose_name_plural = 'Etnias de cada asociado'

    def __unicode__(self): 
        return self.etnia


class HechoAsociado(models.Model):
    asociado = models.ForeignKey('AsociadoDeclarante')
    hecho = models.ForeignKey('generales.HechoVictimizario')

    class Meta: 
        verbose_name_plural = 'Hechos victimizarios por asociado'

    def __unicode__(self): 
        return self.asociado


class HechoDeclarante(models.Model):
    hecho = models.ForeignKey('generales.HechoVictimizario', blank=True, null=True)
    declaracion = models.ForeignKey('TomaDeclaracion')
    cantidad_eventos = models.IntegerField()

    class Meta: 
        verbose_name_plural = 'Hechos victimizarios del declarante'

    def __unicode__(self): 
        return self.cantidad_eventos


class InformacionSolicitante(models.Model): 
    declaracion = models.ForeignKey('TomaDeclaracion', blank=True, null=True) 
    tipo_documento = models.ForeignKey('generales.TipoDocumento')
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    celular = models.BigIntegerField(blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=1024)
    estado_revision = models.CharField(max_length=20)

    class Meta: 
        verbose_name_plural = 'Informacion de solicitantes'

    def __unicode__(self): 
        return self.nombre


class Intermediario(models.Model):
    tipo_documento = models.ForeignKey('generales.TipoDocumento')
    tipo_intermediario = models.ForeignKey('TipoIntermediario')
    declaracion = models.ForeignKey('TomaDeclaracion', blank=True, null=True)
    primer_nombre_intermediario = models.CharField(max_length=20)
    demas_nombres_intermediario = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido_intermediario = models.CharField(max_length=20)
    segundo_apellido_intermediario = models.CharField(max_length=20, blank=True, null=True)
    numero_documento_intermediario = models.BigIntegerField(unique=True)
    direccion_intermediario = models.CharField(max_length=30, blank=True, null=True)
    telefono_intermediario = models.BigIntegerField(blank=True, null=True)

    class Meta: 
        verbose_name_plural = 'Intermediarios'

    def __unicode__(self): 
        return self.primer_nombre_intermediario


class TipoIntermediario(models.Model):
    tipo_intermediario = models.CharField(max_length=50)
    institucion_perteneciente = models.CharField(max_length=100, blank=True, null=True)

    class Meta: 
        verbose_name_plural = 'Tipos de intermediarios'

    def __unicode__(self): 
        return '%s (%s)' % (self.tipo_intermediario, self.institucion_perteneciente)


class TomaDeclaracion(models.Model):
    lugar_declaracion = models.ForeignKey('generales.LugarDeclaracion', blank=True, null=True)
    entidad = models.ForeignKey('generales.EntidadAtencion', blank=True, null=True)
    verificacion = models.ForeignKey('VerificacionProcedimiento', blank=True, null=True)
    tipo_documento = models.ForeignKey('generales.TipoDocumento')
    descripcion_hecho = models.CharField(max_length=1024, blank=True, null=True)
    fecha_declaracion = models.CharField(max_length=20)
    primer_nombre_declarante = models.CharField(max_length=20)
    demas_nombres_declarante = models.CharField(max_length=100, blank=True, null=True) 
    primer_apellido_declarante = models.CharField(max_length=20) 
    segundo_apellido_declarante = models.CharField(max_length=20, blank=True, null=True)
    numero_documento_declarante = models.BigIntegerField(blank=True, null=True)
    fecha_nacimiento_declarante = models.CharField(max_length=20, blank=True, null=True) 
    direccion_declarante = models.CharField(max_length=50)
    barrio_declarante = models.CharField(max_length=50, blank=True, null=True)
    vereda_declarante = models.CharField(max_length=50, blank=True, null=True)
    departamento_declarante = models.CharField(max_length=30)
    municipio_declarante = models.CharField(max_length=50)
    email_declarante = models.CharField(max_length=50, blank=True, null=True)
    fijo_declarante = models.BigIntegerField(blank=True, null=True)
    celular_declarante = models.BigIntegerField(blank=True, null=True)
    direccion_alt_declarante = models.CharField(max_length=50, blank=True, null=True)
    barrio_alt_declarante = models.CharField(max_length=50, blank=True, null=True)
    vereda_alt_declarante = models.CharField(max_length=50, blank=True, null=True)
    departamento_alt_declarante = models.CharField(max_length=30, blank=True, null=True)
    municipio_alt_declarante = models.CharField(max_length=50, blank=True, null=True)
    email_alt_declarante = models.CharField(max_length=50, blank=True, null=True)
    fijo_alt_declarante = models.BigIntegerField(blank=True, null=True)
    celular_alt_declarante = models.BigIntegerField(blank=True, null=True)
    autorizacion_declarante = models.CharField(max_length=2)
    mensajes_celular_declarante = models.CharField(max_length=2)
    mensajes_fijo_declarante = models.CharField(max_length=2)
    mensajes_email_declarante = models.CharField(max_length=2)
    mensajes_otros_declarante = models.CharField(max_length=50, blank=True, null=True)
    estado_atencion_declarador = models.CharField(max_length=15)

    class Meta: 
        verbose_name_plural = 'Tomas de declaraciones'

    def __unicode__(self):
        return '%s %s %s (%s)' % (self.primer_nombre_declarante, self.primer_apellido_declarante,
            self.segundo_apellido_declarante, self.numero_documento_declarante)


class VerificacionProcedimiento(models.Model):
    declaracion = models.ForeignKey('TomaDeclaracion', blank=True, null=True)
    total_anexos_diligenciados = models.IntegerField(blank=True, null=True)
    total_soportes_aportados = models.IntegerField(blank=True, null=True)
    total_folios_declaracion = models.IntegerField()
    realiza_entrevista_previa = models.CharField(max_length=2, blank=True, null=True)
    declarante_lee_declaracion = models.CharField(max_length=2, blank=True, null=True)
    declarante_orientado_corregir = models.CharField(max_length=2, blank=True, null=True)
    correcciones_incluidas = models.CharField(max_length=2, blank=True, null=True)
    observaciones_funcionario = models.CharField(max_length=250, blank=True, null=True)
    declarante_sabe_firmar = models.CharField(max_length=2, blank=True, null=True)

    class Meta: 
        verbose_name_plural = 'Verificaciones de procedimiento'

    def __unicode__(self): 
        return 'Proc: %s %s' % (self.declaracion, self.total_folios_declaracion)
