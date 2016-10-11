# -*- coding: 850 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.urlresolvers import reverse, resolve
from django.template import RequestContext
from generales.models import *
from beneficios.models import *
from solicitantes.models import *
from generales.forms import *
from django.db.models import Q
from datetime import datetime,date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv


def estado_clientes_view(request):
    sistema = InformacionSolicitante.objects.get(id=0)#se obtiene el registro cero para comprobar si se están aceptando solicitudes
    estado = sistema.descripcion#corresponde al estado actual del sistema de registro de solicitudes por parte de los usuarios
    if request.method == 'GET':
        return render_to_response('control_usuarios.html', 
            locals(), 
            context_instance=RequestContext(request)
        )
    else:
        if "Activo" in estado:
            sistema.descripcion = "Bloqueado"
            sistema.save() 
            estado = sistema.descripcion
        else:
            sistema.descripcion = "Activo"
            sistema.save()
            estado = sistema.descripcion
        return render_to_response(
            'control_usuarios.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    return render_to_response(
        'control_usuarios.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


def lista_lugares_declaracion(request):
    lugares = LugarDeclaracion.objects.all()
    paginator = Paginator(lugares, 15) # muestra 15 contactos por página

    page = request.GET.get('page')
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    return render_to_response(
        'lista_lugares_declaracion.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


def lista_tipos_documentos_generales(request):
    tipos_documentos = TipoDocumento.objects.all()

    return render_to_response(
        'lista_tipos_documentos_generales.html', 
        locals(), 
        context_instance=RequestContext(request)
    )

def lista_notificaciones(request, id):
    titulo = ''
    #obtiene el valor seleccionado por el usuario donde 1 es atendidos, 2 pendientes y 3 en revisión
    if '1' in id:
        atendidos = InformacionSolicitante.objects.filter(estado_revision='Atendido')        
        filtro = atendidos#la variable filtro unifica el resultado independientemente del seleccionado
        #esto se hace para usar una sola plantilla html para cualquier filtro
        titulo = 'Solicitantes atendidos'
    if '2' in id:
        pendientes = InformacionSolicitante.objects.filter(estado_revision='Pendiente')
        filtro = pendientes
        titulo = 'Solicitantes pendientes'
    if '3' in id:
        revisados = InformacionSolicitante.objects.filter(estado_revision='En revision')
        filtro = revisados
        titulo = 'Solicitantes en revisión'
    #hace proceso de paginación por si hay muchos registros para que sean presentados por partes
    paginator = Paginator(filtro, 10) # muestra 10 contactos por página
    page = request.GET.get('page')#obtiene el número de página actual seleccionada por el usuario
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    return render_to_response(
        'lista_notificaciones.html', 
        locals(), 
        context_instance=RequestContext(request)
    )

def notificaciones(request):
    #filtra los registros de solicitudes por el estado actual
    atendidos = InformacionSolicitante.objects.filter(estado_revision='Atendido')
    pendientes = InformacionSolicitante.objects.filter(estado_revision='Pendiente')
    revisados = InformacionSolicitante.objects.filter(estado_revision='En revision')

    atend = len(atendidos)#cuenta cuantos registros hay en cada filtro
    pend = len(pendientes)
    revis = len(revisados)
    return render_to_response(
        'notificaciones.html', 
        locals(), 
        context_instance=RequestContext(request)
    )
    

def add_entidad_atencion(request):
    informacion = "inicializando"
    titulo="Nueva entidad de atención"
    if request.method == 'GET':
        form = entidadAtencionForm()
        ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add.html', 
            ctx, 
            context_instance=RequestContext(request)
        )
    else:
        form = entidadAtencionForm(request.POST) 
        info = "inicializando"
        if form.is_valid():
            form.save()
            informacion = "Guardado"
        else:
            informacion = "Error"
        return render_to_response(
            'add.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
    return render_to_response('add.html', 
        ctx,
        context_instance=RequestContext(request)
    )        


def add_tipo_documento(request):
    if request.method == "POST":
        form = addTipoDocumentoForm(request.POST) 
        info = "inicializando"
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            abreviacion = form.cleaned_data['abreviacion']
            t = TipoDocumento()
            t.nombre = nombre
            t.abreviacion = abreviacion
            t.save()
            info = "Guardado"
        else:
            info= "Error"
        form = addTipoDocumentoForm()
        ctx = {'form':form, 'informacion':info}
        return render_to_response('add.html', 
            ctx, 
            context_instance=RequestContext(request)
        )

    else:
        form = addTipoDocumentoForm()
        ctx = {'form':form}
        return render_to_response('add.html', 
            ctx, 
            context_instance=RequestContext(request)
        )


def matriz(request):    
    
    beneficiosAsociados = BeneficioAsociado.objects.all()
    hechosAsociados = HechoAsociado.objects.all()
    etniasAsociados = EtniaAsociado.objects.all()
    discapacidadesAsociados = DiscapacidadAsociado.objects.all()
    derechos = Derecho.objects.all()
    beneficiosDerechoSeleccionado = BeneficioVictima.objects.all()

    derechosBeneficio = []
    condicionesProblematicas = []
    nombresBeneficios = []
    estadosGestionProgramas = []
    metasProgramas = []
    avancesMetas = []
    indicadores = []
    participacionesNacional = []
    participacionesDepartamental = []
    participacionesMunicipal = []
    cooperacionesInternacional = []
    participacionesOtros = []

    coofinanciacionesNacionales = []
    fosygaEtesa = []
    otrosRecursosNacionales = []
    totalPresupuestosNacionales = []
    coofinanciacionesDepartamentales = []
    otrosRecursosDepartamentales = []
    totalPresupuestosDepartamentales = []
    recursosPropios = []
    sistemasGeneralesParticipaciones = []
    regaliasMunicipales = []
    creditosMunicipales = []
    otrosRecursosMunicipales = []
    totalPresupuestosMunicipales = []
    empresasPrivadas = []
    cooperacionesOtros = []
    otrosOtros = []
    totalPresupuestosOtros = []
    totalPresupuestos = []

    beneficioVictimasDesplazamiento = []
    beneficioVictimasOtros = []
    cantidadAsociadosBeneficio = []

    afrocolombianosDesplazados = []
    romDesplazados = []
    indigenasDesplazados = []
    lgbtiDesplazados = []
    mujeresCabezaHogarDesplazados = []
    discapacitadosDesplazados = []
    adultosMayoresDesplazados = []
    ninosSinAcompanamientoDesplazados = []
    ninosAdolecentesDesplazados = []
    noEnfoqueDesplazados = []
    afrocolombianosOtros = []
    romOtros = []
    indigenasOtros = []
    lgbtiOtros = []
    mujeresCabezaHogarOtros = []
    discapacitadosOtros = []
    adultosMayoresOtros = []
    ninosSinAcompanamientoOtros = []
    ninosAdolecentesOtros = []
    noEnfoqueOtros = []

    datosBeneficio = [] #esta variable es una matriz que almacena los datos solicitados por cada beneficio involucrado
    titulos = [
        "Desplazados","Otros hechos victimizantes","total",
        "Afrocolombianos  ","Indigenas  ",
        "Rom  ","LGBTI  ",
        "Mujeres cabeza de hogar  ", "Poblacion en condicion de discapacidad   ",
        "Adultos mayores  ", "Ninos, ninas y adolescentes  ",
        "Victimas de Desplazamiento Forzado sin enfoque diferencial  ",
        "Afrocolombianos","Indígenas",
        "Rom","LGBTI",
        "Mujeres cabeza de hogar", "Población en condición de discapacidad",
        "Adultos mayores", "Niños, niñas y adolescentes",
        "Víctimas de Desplazamiento Forzado sin enfoque diferencial",
        "Coofinanciacion del Nivel Nacional  ", "FOSYGA y ETESA  ",
        "Otros recursos de la nacion  ", "Total recursos del nivel nacional  ",
        "Coofinanciacion Departamental  ",
        "Otros recursos del departamento  ", "Total recursos del nivel departamental  ",
        "Recursos Propios  ", "Sistema General de Participaciones  ",
        "Regalias  ", "Credito  ",
        "Otros  ", "Total de recursos nivel municipal  ",
        "Empresa Privada  ", "Cooperacion  ",
        "Otros  ","Total de otros recursos  ", "TOTAL",
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad",
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad", 
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad", 
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad", 
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad"
        ]

    for i in beneficiosDerechoSeleccionado:#primer nivel de profundidad
        derechoSeleccionado = Derecho.objects.get(id=1)
        for d in derechos:#segundo nivel de profundidad
            if i.derecho_id == d.id:
                derechoSeleccionado = Derecho.objects.get(id=d.id)
        derechosBeneficio.append(derechoSeleccionado.nombre_derecho)#selecciona el derecho para poder presentar el nombre en la matriz
        condicionesProblematicas.append(i.condiciones_problematica)
        nombresBeneficios.append(i.nombre_programa)
        estadosGestionProgramas.append(i.estado_gestion_programa)
        metasProgramas.append(i.meta_programa)
        avancesMetas.append(i.avance_meta_programa)
        indicadores.append(i.indicadores)
        participacionesNacional.append(i.participacion_nacional)
        participacionesDepartamental.append(i.participacion_departamental)
        participacionesMunicipal.append(i.participacion_municipal)
        cooperacionesInternacional.append(i.cooperacion_internacional)
        participacionesOtros.append(i.participacion_otros)

        sumaPresupuestos = 0 #se suman todos los presupuestos para determinar el valor final
        totalPresupuestoNacionalBeneficio = 0#cuenta el total de presupuesto nacional para cada beneficio
        if i.coofinanciacion_nacional >= 0:
            totalPresupuestoNacionalBeneficio += i.coofinanciacion_nacional
            coofinanciacionesNacionales.append(i.coofinanciacion_nacional)
        else:
            coofinanciacionesNacionales.append(0)
        if i.fosyga_etesa >= 0:
            totalPresupuestoNacionalBeneficio += i.fosyga_etesa
            fosygaEtesa.append(i.fosyga_etesa)
        else:
            fosygaEtesa.append(0)
        if i.otros_recursos_nacionales >= 0:
            totalPresupuestoNacionalBeneficio += i.otros_recursos_nacionales
            otrosRecursosNacionales.append(i.otros_recursos_nacionales)
        else:
            otrosRecursosNacionales.append(0)
        totalPresupuestosNacionales.append(totalPresupuestoNacionalBeneficio)
        sumaPresupuestos += totalPresupuestoNacionalBeneficio

        totalPresupuestoDepartamentalBeneficio = 0#cuenta el total de presupuesto departamental para cada beneficio
        if i.coofinanciacion_departamental >= 0:
            totalPresupuestoDepartamentalBeneficio += i.coofinanciacion_departamental
            coofinanciacionesDepartamentales.append(i.coofinanciacion_departamental)
        else:
            coofinanciacionesDepartamentales.append(0)
        if i.otros_recursos_departamentales >= 0:
            totalPresupuestoDepartamentalBeneficio += i.otros_recursos_departamentales
            otrosRecursosDepartamentales.append(i.otros_recursos_departamentales)
        else:
            otrosRecursosDepartamentales.append(0)
        totalPresupuestosDepartamentales.append(totalPresupuestoDepartamentalBeneficio)
        sumaPresupuestos += totalPresupuestoDepartamentalBeneficio

        totalPresupuestoMunicipalBeneficio = 0#cuenta el total de presupuesto municipal para cada beneficio
        if i.recursos_propios >= 0:
            totalPresupuestoMunicipalBeneficio += i.recursos_propios
            recursosPropios.append(i.recursos_propios)
        else:
            recursosPropios.append(0)
        if i.sistema_general_participacion >= 0:
            totalPresupuestoMunicipalBeneficio += i.sistema_general_participacion
            sistemasGeneralesParticipaciones.append(i.sistema_general_participacion)
        else:
            sistemasGeneralesParticipaciones.append(0)
        if i.regalia >= 0:
            totalPresupuestoMunicipalBeneficio += i.regalia
            regaliasMunicipales.append(i.regalia)
        else:
            regaliasMunicipales.append(0)
        if i.credito >= 0:
            totalPresupuestoMunicipalBeneficio += i.credito
            creditosMunicipales.append(i.credito)
        else:
            creditosMunicipales.append(0)
        if i.otros_recursos_municipales >= 0:
            totalPresupuestoMunicipalBeneficio += i.otros_recursos_municipales
            otrosRecursosMunicipales.append(i.otros_recursos_municipales)
        else:
            otrosRecursosMunicipales.append(0)
        totalPresupuestosMunicipales.append(totalPresupuestoMunicipalBeneficio)
        sumaPresupuestos += totalPresupuestoMunicipalBeneficio

        totalPresupuestoOtrosBeneficio = 0#cuenta el total de otros presupuestos para cada beneficio
        if i.empresa_privada >= 0:
            totalPresupuestoOtrosBeneficio += i.empresa_privada
            empresasPrivadas.append(i.empresa_privada)
        else:
            empresasPrivadas.append(0)
        if i.cooperacion_otros >= 0:
            totalPresupuestoOtrosBeneficio += i.cooperacion_otros
            cooperacionesOtros.append(i.cooperacion_otros)
        else:
            cooperacionesOtros.append(0)
        if i.otros >= 0:
            totalPresupuestoOtrosBeneficio += i.otros
            otrosOtros.append(i.otros)
        else:
            otrosOtros.append(0)
        totalPresupuestosOtros.append(totalPresupuestoOtrosBeneficio)
        sumaPresupuestos += totalPresupuestoOtrosBeneficio

        totalPresupuestos.append(sumaPresupuestos)

        cantidad = 0
        victimasDesplazamiento = 0
        victimasOtros = 0
        beneficioAfrocolombianosDesplazados = 0
        beneficioAfrocolombianosOtros = 0
        beneficioRomDesplazados = 0
        beneficioRomOtros = 0
        beneficioIndigenasDesplazados = 0
        beneficioIndigenasOtros = 0
        beneficioLgbtiDesplazados = 0
        beneficioLgbtiOtros = 0
        beneficiomujeresCabezaDesplazados = 0
        beneficiomujeresCabezaOtros = 0
        beneficioDiscapacitadosDesplazados = 0
        beneficioDiscapacitadosOtros = 0
        beneficioAdultosMayoresDesplazados = 0
        beneficioAdultosMayoresOtros = 0
        beneficioNinosSinAcompanamientoDesplazados = 0
        beneficioNinosSinAcompanamientoOtros = 0
        beneficioNinosAdolecentesDesplazados = 0
        beneficioNinosAdolecentesOtros = 0
        beneficioNoEnfoqueDesplazados = 0
        beneficioNoEnfoqueOtros = 0

        for j in beneficiosAsociados:#segundo nivel de profundidad
            if i.id == j.beneficio_id:#compara si el beneficiario corresponde al beneficio mediante la entidad debil BeneficioAsociado
                if "Atendido" in j.estado_actual_beneficio:#solo cuenta a las personas que han sido atendidads
                    cantidad = cantidad + 1
                    repeticionDesplazamiento = 0 #evita que se cuente a la misma persona como desplazada mas de una vez
                    repeticionOtros = 0 #evita que se cuente a la misma persona como victima de otros mas de una vez
                    
                    for k in hechosAsociados:
                        if  j.asociado_id == k.asociado_id:#compara al asociado actual con los hechos victimizarios
                            asociadoSeleccionado = AsociadoDeclarante.objects.get(id=j.asociado_id)
                            if k.hecho_id == 5:#el hecho 5 corresponde a desplazamiento forzado
                                conteoNoEnfoque = 0 #verifica si no pertenece a ningun enfoque diferencial 
                                
                                if repeticionDesplazamiento  == 0:
                                    victimasDesplazamiento += 1
                                    repeticionDesplazamiento = 1 
                                    for l in etniasAsociados: #verifica si pertenece a una o mas grupos etnicos
                                        if  l.asociado_id == j.asociado_id:
                                            if  l.etnia_id == 1 or l.etnia_id == 2:# si corresponde a una comunidad afrocolombiana
                                                beneficioAfrocolombianosDesplazados += 1
                                                conteoNoEnfoque += 1
                                            if  l.etnia_id == 3 or l.etnia_id == 4:# si corresponde a una comunidad gitana
                                                beneficioRomDesplazados += 1
                                                conteoNoEnfoque += 1
                                            if  l.etnia_id == 5 or l.etnia_id == 6 or l.etnia_id == 7:# si corresponde a una comunidad indigena
                                                beneficioIndigenasDesplazados += 1
                                                conteoNoEnfoque += 1
                                            
                                    if asociadoSeleccionado.genero_id == 1013:#verifica si el genero del asociado es LGBTI
                                        beneficioLgbtiDesplazados += 1
                                        conteoNoEnfoque += 1
                                    if "SI" in asociadoSeleccionado.mujer_cabeza_familia:#verifica si es mujer cabeza de hogar
                                        beneficiomujeresCabezaDesplazados += 1
                                        conteoNoEnfoque += 1
                                    conteoDiscapacidades = 0
                                    for m in discapacidadesAsociados: #verifica si tiene una o mas discapacidades
                                        if  m.asociado_id == j.asociado_id:
                                            conteoDiscapacidades += 1
                                    if conteoDiscapacidades != 0:
                                        beneficioDiscapacitadosDesplazados += 1
                                        conteoNoEnfoque += 1
                                    fecha_nacimiento = datetime.strptime(asociadoSeleccionado.fecha_nacimiento_asociado, "%d-%m-%Y")
                                    edad = datetime.now() - fecha_nacimiento # calcula en dias la edad del asociado
                                    if edad.days >= 21900:#verifica si es adulto mayor
                                        beneficioAdultosMayoresDesplazados += 1
                                        conteoNoEnfoque += 1
                                    if edad.days <= 6574:#verifica si es menor de edad
                                        beneficioNinosAdolecentesDesplazados += 1
                                        conteoNoEnfoque += 1
                                    if conteoNoEnfoque == 0:#verifica si no pertenece a ningun enfoque diferencial 
                                        beneficioNoEnfoqueDesplazados += 1

                            else:#si es un hecho distinto a desplazamiento forzado
                                conteoNoEnfoque = 0 
                                if repeticionOtros  == 0:
                                    victimasOtros += 1
                                    repeticionOtros = 1 
                                    for l in etniasAsociados: #verifica si pertenece a una o mas grupos etnicos
                                        
                                        if  l.asociado_id == j.asociado_id:
                                            if  l.etnia_id == 1 or l.etnia_id == 2:# si corresponde a una comunidad afrocolombiana
                                                beneficioAfrocolombianosOtros += 1
                                                conteoNoEnfoque += 1
                                            if  l.etnia_id == 3 or l.etnia_id == 4:# si corresponde a una comunidad gitana
                                                beneficioRomOtros += 1
                                                conteoNoEnfoque += 1
                                            if  l.etnia_id == 5 or l.etnia_id == 6 or l.etnia_id == 7:# si corresponde a una comunidad indigena
                                                beneficioIndigenasOtros += 1
                                                conteoNoEnfoque += 1
                                            
                                    if asociadoSeleccionado.genero_id == 1013:#verifica si el genero del asociado es LGBTI
                                        beneficioLgbtiOtros += 1
                                        conteoNoEnfoque += 1
                                    if "SI" in asociadoSeleccionado.mujer_cabeza_familia:#verifica si es mujer cabeza de hogar
                                        beneficiomujeresCabezaOtros += 1
                                        conteoNoEnfoque += 1
                                    conteoDiscapacidades = 0
                                    for m in discapacidadesAsociados: #verifica si tiene una o mas discapacidades
                                        if  m.asociado_id == j.asociado_id:
                                            conteoDiscapacidades += 1
                                    if conteoDiscapacidades != 0:
                                        beneficioDiscapacitadosOtros += 1
                                        conteoNoEnfoque += 1
                                    fecha_nacimiento = datetime.strptime(asociadoSeleccionado.fecha_nacimiento_asociado, "%d-%m-%Y")
                                    edad = datetime.now() - fecha_nacimiento # calcula en dias la edad del asociado
                                    if edad.days >= 21900:#verifica si es adulto mayor
                                        beneficioAdultosMayoresOtros += 1
                                        conteoNoEnfoque += 1
                                    if edad.days <= 6574:#verifica si es menor de edad
                                        beneficioNinosAdolecentesOtros += 1
                                        conteoNoEnfoque += 1
                                    if conteoNoEnfoque == 0:
                                        beneficioNoEnfoqueOtros += 1


        beneficioVictimasDesplazamiento.append(victimasDesplazamiento)#victimas de desplazamiento encontradas por cada beneficio
        beneficioVictimasOtros.append(victimasOtros)#victimas de otros encontradas por cada beneficio
        cantidadAsociadosBeneficio.append(cantidad) #cuenta el total de victimas correspondientes a desplazamiento y otros hechos
        afrocolombianosDesplazados.append(beneficioAfrocolombianosDesplazados)
        afrocolombianosOtros.append(beneficioAfrocolombianosOtros)
        romDesplazados.append(beneficioRomDesplazados)
        romOtros.append(beneficioRomOtros)
        indigenasDesplazados.append(beneficioIndigenasDesplazados)
        indigenasOtros.append(beneficioIndigenasOtros)
        lgbtiDesplazados.append(beneficioLgbtiDesplazados)
        lgbtiOtros.append(beneficioLgbtiOtros)
        mujeresCabezaHogarDesplazados.append(beneficiomujeresCabezaDesplazados)
        mujeresCabezaHogarOtros.append(beneficiomujeresCabezaOtros)
        discapacitadosDesplazados.append(beneficioDiscapacitadosDesplazados)
        discapacitadosOtros.append(beneficioDiscapacitadosOtros)
        adultosMayoresDesplazados.append(beneficioAdultosMayoresDesplazados)
        adultosMayoresOtros.append(beneficioAdultosMayoresOtros)
        #ninosSinAcompanamientoDesplazados = []
        #ninosSinAcompanamientoOtros = []
        ninosAdolecentesDesplazados.append(beneficioNinosAdolecentesDesplazados)
        ninosAdolecentesOtros.append(beneficioNinosAdolecentesOtros)
        noEnfoqueDesplazados.append(beneficioNoEnfoqueDesplazados)
        noEnfoqueOtros.append(beneficioNoEnfoqueOtros)
    index = 0
    for ben in beneficiosDerechoSeleccionado:#recorre y almacena los datos de los beneficios correspondientes al derecho
        vector = [
        derechosBeneficio[index],
        condicionesProblematicas[index], nombresBeneficios[index],
        estadosGestionProgramas[index], metasProgramas[index],
        avancesMetas[index], indicadores[index],
        beneficioVictimasDesplazamiento[index], beneficioVictimasOtros[index], cantidadAsociadosBeneficio[index],
        afrocolombianosDesplazados[index], indigenasDesplazados[index],
        romDesplazados[index], lgbtiDesplazados[index],
        mujeresCabezaHogarDesplazados[index], discapacitadosDesplazados[index],
        adultosMayoresDesplazados[index], ninosAdolecentesDesplazados[index],
        noEnfoqueDesplazados[index],
        afrocolombianosOtros[index], indigenasOtros[index],
        romOtros[index], lgbtiOtros[index],
        mujeresCabezaHogarOtros[index], discapacitadosOtros[index],
        adultosMayoresOtros[index], ninosAdolecentesOtros[index],
        noEnfoqueOtros[index],
        coofinanciacionesNacionales[index], fosygaEtesa[index], 
        otrosRecursosNacionales[index], totalPresupuestosNacionales[index],
        coofinanciacionesDepartamentales[index], 
        otrosRecursosDepartamentales[index], totalPresupuestosDepartamentales[index],
        recursosPropios[index], sistemasGeneralesParticipaciones[index],
        regaliasMunicipales[index], creditosMunicipales[index],
        otrosRecursosMunicipales[index], totalPresupuestosMunicipales[index],
        empresasPrivadas[index], cooperacionesOtros[index], otrosOtros[index],
        totalPresupuestosOtros[index], totalPresupuestos[index],
        participacionesNacional[index], participacionesDepartamental[index],
        participacionesMunicipal[index], cooperacionesInternacional[index], participacionesOtros[index]
        ]

        datosBeneficio.append(vector)
        index = index + 1

    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="matriz.csv"'
        
        head = [
        "Derechos","Condiciones de la problematica territorial","Nombre del programa/proyecto y/o actividad",
        "Estado de gestión del programa/proyecto y/o actividad","Meta del programa y/o proyecto",
        "Avance de la meta del programa y/o proyecto","Indicador (es)",
        "Desplazados","Otros hechos victimizantes","total",
        "Afrocolombianos  ","Indigenas  ",
        "Rom  ","LGBTI  ",
        "Mujeres cabeza de hogar  ", "Poblacion en condicion de discapacidad   ",
        "Adultos mayores  ", "Ninos, ninas y adolescentes  ",
        "Victimas de Desplazamiento Forzado sin enfoque diferencial  ",
        "Afrocolombianos","Indígenas",
        "Rom","LGBTI",
        "Mujeres cabeza de hogar", "Población en condición de discapacidad",
        "Adultos mayores", "Niños, niñas y adolescentes",
        "Víctimas de Desplazamiento Forzado sin enfoque diferencial",
        "Coofinanciacion del Nivel Nacional  ", "FOSYGA y ETESA  ",
        "Otros recursos de la nacion  ", "Total recursos del nivel nacional  ",
        "Coofinanciacion Departamental  ",
        "Otros recursos del departamento  ", "Total recursos del nivel departamental  ",
        "Recursos Propios  ", "Sistema General de Participaciones  ",
        "Regalias  ", "Credito  ",
        "Otros  ", "Total de recursos nivel municipal  ",
        "Empresa Privada  ", "Cooperacion  ",
        "Otros  ","Total de otros recursos  ", "TOTAL",
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad",
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad", 
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad", 
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad", 
        "Descripción de la participación de la entidad en la ejecución del programa/proyecto/actividad"
        ]
        
        writer = csv.writer(response, delimiter=';')
        writer.writerow(head)
        for i in datosBeneficio:
            writer.writerow(i)

        return response
    return render_to_response('matriz_beneficios.html', 
        locals(), 
        context_instance=RequestContext(request)
    )
    

@login_required
def index_view(request):
    return render_to_response('index.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


def login_view(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', 
            locals(), 
            context_instance=RequestContext(request)
        )
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('index.html', 
                    locals(), 
                    context_instance=RequestContext(request)
                )
            else:
                pass
        mensaje = 'El nombre usuario y/o la clave no son correctos'
    return render_to_response('login.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


def logout_view(request):
    logout(request)
    #messages.success(request, 'Desconectado satisfactoriamente')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('index.html', 
                    locals(), 
                    context_instance=RequestContext(request)
                )
            else:
                pass
        mensaje = 'nombre o contrasena invalidos'
    return render_to_response('login.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


def add_lugar_declaracion(request):
    informacion = "inicializando"
    titulo="Nuevo lugar de declaración"
    if request.method == 'GET':
        form = lugarDeclaracionForm()
        ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add.html', 
            ctx, 
            context_instance=RequestContext(request)
        )
    else:
        form = lugarDeclaracionForm(request.POST) 
        info = "inicializando"
        if form.is_valid():
            form.save()
            informacion = "Guardado"
        else:
            informacion = "Error"
        return render_to_response(
            'add.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
    return render_to_response('add.html', 
        ctx,
        context_instance=RequestContext(request)
    ) 


