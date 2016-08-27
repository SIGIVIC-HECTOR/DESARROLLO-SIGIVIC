from django.contrib import admin
from solicitantes.models import InformacionSolicitante
from solicitantes.models import TomaDeclaracion
from solicitantes.models import VerificacionProcedimiento
from solicitantes.models import AsociadoDeclarante
from solicitantes.models import BeneficioAsociado
from solicitantes.models import HechoDeclarante
from solicitantes.models import Intermediario
from solicitantes.models import TipoIntermediario
from solicitantes.models import HechoAsociado
from solicitantes.models import DiscapacidadAsociado
from solicitantes.models import EtniaAsociado
from solicitantes.models import CorreccionDeclaracion

admin.site.register(InformacionSolicitante)
admin.site.register(TomaDeclaracion)
admin.site.register(VerificacionProcedimiento)
admin.site.register(AsociadoDeclarante)
admin.site.register(BeneficioAsociado)
admin.site.register(HechoDeclarante)
admin.site.register(Intermediario)
admin.site.register(TipoIntermediario)
admin.site.register(HechoAsociado)
admin.site.register(DiscapacidadAsociado)
admin.site.register(EtniaAsociado)
admin.site.register(CorreccionDeclaracion)