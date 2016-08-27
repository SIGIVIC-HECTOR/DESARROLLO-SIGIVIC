from django.contrib import admin
from generales.models import TipoDocumento
from generales.models import LugarDeclaracion
from generales.models import EntidadAtencion
from generales.models import EstadoCivil
from generales.models import Genero
from generales.models import PreferenciaEtnica
from generales.models import Discapacidad
from generales.models import RegimenEspecial
from generales.models import Parentezco
from generales.models import HechoVictimizario

admin.site.register(TipoDocumento)
admin.site.register(LugarDeclaracion)
admin.site.register(EntidadAtencion)
admin.site.register(EstadoCivil)
admin.site.register(Genero)
admin.site.register(PreferenciaEtnica)
admin.site.register(Discapacidad)
admin.site.register(RegimenEspecial)
admin.site.register(Parentezco)
admin.site.register(HechoVictimizario)