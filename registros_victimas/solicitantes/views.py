# -*- coding: 850 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from solicitantes.models import *
from beneficios.models import *
from solicitantes.forms import *
from django.forms import ModelForm
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
import time

logger = logging.getLogger(__name__)

"""La función hace una captura de la entidad DeclarantesRegistrados de la base de datos y presenta todos sus registros
en una lista paginada."""
def lista_declarantes(request):
    declaraciones = TomaDeclaracion.objects.all()
    paginator = Paginator(declaraciones, 10) # muestra 10 contactos por página

    page = request.GET.get('page')
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    return render_to_response(
        'lista_declarantes.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


"""La función hace una captura de la entidad Solicitudes de la base de datos y presenta todos sus registros
en una lista paginada."""
def lista_solicitantes(request):
    solicitantes = InformacionSolicitante.objects.all()
    paginator = Paginator(solicitantes, 10) # muestra 10 contactos por página

    page = request.GET.get('page')
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    return render_to_response(
        'lista_solicitantes.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


"""La función hace una captura de la entidad AsociadosDeclarante de la base de datos y presenta todos sus registros
en una lista paginada."""
def lista_asociados_declarante(request, id):
    asociados = AsociadoDeclarante.objects.filter(declaracion__id=id)
    declarante = TomaDeclaracion.objects.get(id=id)
    return render_to_response(
        'lista_asociados_declarante.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


"""La función hace una captura de la entidad Intermediarios de la base de datos y presenta todos sus registros
en una lista paginada."""
def lista_intermediarios(request):
    intermediarios = Intermediario.objects.all()
    paginator = Paginator(intermediarios, 10) # muestra 10 contactos por página

    page = request.GET.get('page')
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    return render_to_response(
        'lista_intermediarios.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_asociado(request):
    informacion = "inicializando"
    titulo="Nuevo asociado"    
    if request.method == 'GET':
        form = asociadoForm()
        ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add.html', 
            ctx,
            context_instance=RequestContext(request)
        )
    else:
        form = asociadoForm(request.POST)
        try:
            mydate = time.strptime(request.POST['fecha_nacimiento_asociado'], '%d-%m-%Y')
            if form.is_valid():
                form.save()
                informacion = "Guardado"
            else:
                informacion = "Error"
        except Exception, e:
            informacion = "DateError"
        
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


"""La función captura un registro de la entidad seleccionado para ser modificado a partir de su identificador, presenta
un formulario estructurado a partir del modelo correspondiente con los campos presentados en el registro y permite hacer
cambios para luego ser almacenados en la base de datos."""
def update_asociado_declarante(request, id):
    print "asociado"
    print id
    asociado = AsociadoDeclarante.objects.get(id=id)
    informacion = "Procesando"
    titulo="Actualizar datos del asociado"

    hechosAsociado = HechoAsociado.objects.filter(asociado_id=id)#busca los hechos victimizarios relacionados al asociado
    hechosVictimizarios = HechoVictimizario.objects.all()
    ids = []#guarda el id de cada hecho para poder modificarlo posteriormente
    nombres = []#guarda los nombres de los hechos victimizarios asociados
    hechos = []
    for i in hechosAsociado:
        for j in hechosVictimizarios:
            if i.hecho_id == j.id:
                nombres.append(j.descripcion_hecho)
                ids.append(i.id)

    index = 0
    for i in hechosAsociado:
        var = [nombres[index], ids[index]]
        hechos.append(var)
        index += 1
    
    beneficiosAsociado = BeneficioAsociado.objects.filter(asociado_id=id)#busca los beneficios relacionados al asociado
    beneficiosVictima = BeneficioVictima.objects.all()
    ids = []#guarda el id de cada beneficio para poder modificarlo posteriormente
    nombres = []#almacena el nombre de los beneficios
    estados = []#almacena los estados actuales de cada beneficio al que se encuentra registrado el asociado
    beneficios = []
    for i in beneficiosAsociado:#busca los beneficios del asociado
        for j in beneficiosVictima:
            if i.beneficio_id == j.id:
                nombres.append(j.nombre_programa)
                estados.append(i.estado_actual_beneficio)
                ids.append(i.id)
    index = 0
    for i in beneficiosAsociado:
        var = [nombres[index], estados[index], ids[index]]
        beneficios.append(var)
        index += 1

    etniasAsociado = EtniaAsociado.objects.filter(asociado_id=id)#busca los grupos etnicos a los que pertenece el asociado
    preferenciasEtnicas = PreferenciaEtnica.objects.all()
    ids = []#guarda el id de cada etnia para poder modificarlo posteriormente
    nombres = []#almacena el nombre de las etnias
    etnias = []
    for i in etniasAsociado:#busca loas etnias del asociado
        for j in preferenciasEtnicas:
            if i.etnia_id == j.id:
                nombres.append(j.nombre_etnia)
                ids.append(i.id)
    index = 0
    for i in etniasAsociado:
        var = [nombres[index], ids[index]]
        etnias.append(var)
        index += 1

    discapacidadesAsociado = DiscapacidadAsociado.objects.filter(asociado_id=id)#busca las discapacidades que registra el asociado
    discapacidadesVictima = Discapacidad.objects.all()
    ids = []#guarda el id de cada discapacidad para poder modificarlo posteriormente
    nombres = []#almacena el nombre de las discapacidades
    discapacidades = []
    for i in discapacidadesAsociado:#busca las discapacidades del asociado
        for j in discapacidadesVictima:
            if i.discapacidad_id == j.id:
                nombres.append(j.tipo_discapacidad)
                ids.append(i.id)
    index = 0
    for i in discapacidadesAsociado:
        var = [nombres[index], ids[index]]
        discapacidades.append(var)
        index += 1

    if request.method == 'GET':
        form = asociadoForm(instance=asociado)
    else:
        form = asociadoForm(request.POST, instance=asociado)
        try:
            mydate = time.strptime(request.POST['fecha_nacimiento_asociado'], '%d-%m-%Y')
            if form.is_valid():
                form.save()
                informacion = "Guardado"
            else:
                informacion = "Error"
        except Exception, e:
            informacion = "DateError"
        return render_to_response(
            'add_form_asociados.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    return render_to_response('add_form_asociados.html', 
        locals(),
        context_instance=RequestContext(request)
    )
  

"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_beneficio_asociado(request, id):
    informacion = "inicializando"
    titulo="Asignar beneficio"
    if request.method == 'GET':
        form = beneficioAsociadoForm()
        ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add.html', 
            ctx,
            context_instance=RequestContext(request)
        )
    else:
        form = beneficioAsociadoForm(request.POST)
        if form.is_valid():
            beneficio = form.save(commit=False)
            beneficio.asociado_id = id
            beneficio.save()#se almacena el hecho victimizario del declarante
            informacion = "Guardado"
            return render_to_response(
                'volver_asociado.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función realiza una consulta en la base de datos a partir de un identificador para determinar el registro seleccionado,
una vez encontrado se procede a eliminar."""
def delete_beneficio_asociado(request, idben, id):
    beneficio = BeneficioAsociado.objects.get(id=idben)
    informacion = 'Procesando'
    if request.method == 'GET':
        beneficio.delete()
        informacion = 'Eliminado'
    return render_to_response(
        'volver_asociado.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función captura un registro de la entidad seleccionado para ser modificado a partir de su identificador, presenta
un formulario estructurado a partir del modelo correspondiente con los campos presentados en el registro y permite hacer
cambios para luego ser almacenados en la base de datos."""
def update_beneficio_asociado(request, idben, id):
    beneficios = BeneficioAsociado.objects.get(id=idben)
    informacion = "Procesando"
    titulo="Actualizar datos del beneficio otorgado"
    if request.method == 'GET':
        form = beneficioAsociadoForm(instance=beneficios)
    else:
        form = beneficioAsociadoForm(request.POST, instance=beneficios)
        if form.is_valid():
            form.save()
            informacion = "Guardado"
            return render_to_response(
                'volver_asociado.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_correccion_declaracion(request):
    informacion = "inicializando"
    titulo="Anexar corrección"
    if request.method == 'GET':
        form = correccionDeclaracionForm()
        ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add.html', 
            ctx,
            context_instance=RequestContext(request)
        )
    else:
        form = correccionDeclaracionForm(request.POST)
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
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función agrega un nuevo registro a la entidad TomaDeclaracion, a su vez crea dos nuevos registros en las entidades Asociados 
y VerificacionProcedimiento, los cuales se relacionan directamente con el registro principal, se integran tres formularios
los cuales son estructurados a partir de los modelos correspondientes de la base de datos, una vez validados estos, se 
almacenan simultaneamente."""
def add_declaracion(request):
    informacion = "inicializando"
    titulo="Nuevo declarante"
    if request.method == 'GET':
        form = declaracionForm()
        form2 = verificacionProcedimientoForm()
        form3 = declaranteAsociadoForm()
        ctx = {'form':form, 'form2':form2, 'form3':form3, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add_declarante.html', 
            ctx,
            context_instance=RequestContext(request)
        )
    else:
        form = declaracionForm(request.POST)
        form2 = verificacionProcedimientoForm(request.POST)
        form3 = declaranteAsociadoForm(request.POST)
                
        try:
            mydate = time.strptime(request.POST['fecha_nacimiento_declarante'], '%d-%m-%Y')
            mydate2 = time.strptime(request.POST['fecha_declaracion'], '%d-%m-%Y')
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                declar = form.save()
                verif = form2.save()
                declar.verificacion_id = verif.id
                verif.declaracion_id=declar.id
                declar.save()
                verif.save()
                asoc = form3.save(commit=False)
                asoc.declaracion_id=declar.id
                asoc.primer_nombre_asociado = declar.primer_nombre_declarante
                asoc.demas_nombres_asociado = declar.demas_nombres_declarante
                asoc.primer_apellido_asociado = declar.primer_apellido_declarante
                asoc.segundo_apellido_asociado = declar.segundo_apellido_declarante
                asoc.numero_documento_asociado = declar.numero_documento_declarante
                asoc.fecha_nacimiento_asociado = declar.fecha_nacimiento_declarante
                asoc.estado_atencion_asociado = declar.estado_atencion_declarador
                asoc.tipo_documento_id = declar.tipo_documento_id
                asoc.parentezco_id = 1014#parentezco declarante
                asoc.save()
                informacion = "Guardado"
            else:
                informacion = "Error"
        except Exception, e:
            informacion = "DateError"
        return render_to_response(
            'add_declarante.html', 
            locals(),
            context_instance=RequestContext(request)
        )


"""La función hace uso de tres identificadores correspondientes a la declaración, verificación de procedimiento y asociado para
construir los formularios con los datos actuales y permitir hacer modificaciones en uno o más campos de cualquiera de estos."""
def update_declarante(request, id):
    declarante = TomaDeclaracion.objects.get(id=id)
    verificacion = VerificacionProcedimiento.objects.get(declaracion_id=id)
    asociado = AsociadoDeclarante.objects.get(numero_documento_asociado=declarante.numero_documento_declarante)
    informacion = "Procesando"
    hechosDeclarante = HechoDeclarante.objects.filter(declaracion_id=id)#busca los hechos victimizarios relacionados al declarante
    hechosVictimizarios = HechoVictimizario.objects.all()
    nombres = []#almacena el nombre de los hechos
    cantidad = []#almacena la cantidad de sucesos asociados a cada hecho
    ids = []#almacena el identificador de cada hecho victimizario relacionado con el declarante
    hechos = []
    for i in hechosDeclarante:
        for j in hechosVictimizarios:
            if i.hecho_id == j.id:
                nombres.append(j.descripcion_hecho)
                cadena = str(i.cantidad_eventos) + ' veces'
                cantidad.append(cadena)
                ids.append(i.id)
    index = 0
    for i in hechosDeclarante:
        var = [nombres[index], cantidad[index], ids[index]]
        hechos.append(var)
        index += 1


    titulo="Actualizar datos del declarante"
    if request.method == 'GET':
        form = declaracionForm(instance=declarante)
        form2 = verificacionProcedimientoForm(instance=verificacion)
        form3 = declaranteAsociadoForm(instance=asociado)
    else:
        form = declaracionForm(request.POST, instance=declarante)
        form2 = verificacionProcedimientoForm(request.POST, instance=verificacion)
        form3 = declaranteAsociadoForm(request.POST, instance=asociado)
        
        try:
            mydate = time.strptime(request.POST['fecha_nacimiento_declarante'], '%d-%m-%Y')
            mydate2 = time.strptime(request.POST['fecha_declaracion'], '%d-%m-%Y')
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                declar = form.save()
                form2.save()
                asoc = form3.save(commit=False)
                asoc.declaracion_id=declar.id
                asoc.primer_nombre_asociado = declar.primer_nombre_declarante
                asoc.demas_nombres_asociado = declar.demas_nombres_declarante
                asoc.primer_apellido_asociado = declar.primer_apellido_declarante
                asoc.segundo_apellido_asociado = declar.segundo_apellido_declarante
                asoc.numero_documento_asociado = declar.numero_documento_declarante
                asoc.fecha_nacimiento_asociado = declar.fecha_nacimiento_declarante
                asoc.estado_atencion_asociado = declar.estado_atencion_declarador
                asoc.tipo_documento_id = declar.tipo_documento_id
                asoc.parentezco_id = 1014#parentezco declarante
                asoc.save()
                informacion = "Guardado"
            else:
                informacion = "Error"
        except Exception, e:
            informacion = "DateError"
        return render_to_response(
            'add_declarante_hechos.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    ctx = {'form':form, 'form2':form2, 'form3':form3, 'hechos':hechos, 'declarante':declarante, 'informacion':informacion, 'titulo': titulo}
    return render_to_response('add_declarante_hechos.html', 
        ctx,
        context_instance=RequestContext(request)
    )


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_discapacidad_asociado(request, id):
    print id
    informacion = "inicializando"
    titulo="Asignar discapacidad"
    if request.method == 'GET':
        form = discapacidadAsociadoForm()
        return render_to_response('add.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    else:
        form = discapacidadAsociadoForm(request.POST)
        if form.is_valid():
            discapacidad = form.save(commit=False)
            discapacidad.asociado_id = id
            discapacidad.save()#se almacena la etnia del declarante
            informacion = "Guardado"
            return render_to_response(
                'volver_asociado.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función realiza una consulta en la base de datos a partir de un identificador para determinar el registro seleccionado,
una vez encontrado se procede a eliminar."""
def delete_discapacidad_asociado(request, iddisc, id):
    discapacidad = DiscapacidadAsociado.objects.get(id=iddisc)
    informacion = 'Procesando'
    if request.method == 'GET':
        discapacidad.delete()
        informacion = 'Eliminado'
        return render_to_response(
                'volver_asociado.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response(
        'volver_asociado.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función captura un registro de la entidad seleccionado para ser modificado a partir de su identificador, presenta
un formulario estructurado a partir del modelo correspondiente con los campos presentados en el registro y permite hacer
cambios para luego ser almacenados en la base de datos."""
def update_discapacidad_asociado(request, iddisc, id):
    discapacidades = DiscapacidadAsociado.objects.get(id=iddisc)
    informacion = "Procesando"
    titulo="Actualizar datos de la etnia"
    if request.method == 'GET':
        form = discapacidadAsociadoForm(instance=discapacidades)
    else:
        form = discapacidadAsociadoForm(request.POST, instance=discapacidades)
        if form.is_valid():
            form.save()
            informacion = "Guardado"
            return render_to_response(
                'volver_asociado.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_etnia_asociado(request, id):
    informacion = "inicializando"
    titulo="Asignar etnia"
    if request.method == 'GET':
        form = etniaAsociadoForm()
        return render_to_response('add.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    else:
        form = etniaAsociadoForm(request.POST)
        if form.is_valid():
            etnia = form.save(commit=False)
            etnia.asociado_id = id
            etnia.save()#se almacena la etnia del declarante
            informacion = "Guardado"
            return render_to_response(
                'volver_asociado.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función realiza una consulta en la base de datos a partir de un identificador para determinar el registro seleccionado,
una vez encontrado se procede a eliminar."""
def delete_etnia_asociado(request, idet, id):
    etnia = EtniaAsociado.objects.get(id=idet)
    informacion = 'Procesando'
    if request.method == 'GET':
        etnia.delete()
        informacion = 'Eliminado'
    return render_to_response(
        'volver_asociado.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función captura un registro de la entidad seleccionado para ser modificado a partir de su identificador, presenta
un formulario estructurado a partir del modelo correspondiente con los campos presentados en el registro y permite hacer
cambios para luego ser almacenados en la base de datos."""
def update_etnia_asociado(request, idet, id):
    etnias = EtniaAsociado.objects.get(id=idet)
    informacion = "Procesando"
    titulo="Actualizar datos de la etnia"
    if request.method == 'GET':
        form = etniaAsociadoForm(instance=etnias)
    else:
        form = etniaAsociadoForm(request.POST, instance=etnias)
        if form.is_valid():
            form.save()
            informacion = "Guardado"
            return render_to_response(
                'volver_asociado.html', 
                locals(),
                context_instance=RequestContext(request)
            )
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


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_hecho_declarante(request, id):
    informacion = "inicializando"
    titulo="Nuevo hecho victimizario"
    if request.method == 'GET':
        form = hechoDeclaranteForm()
        return render_to_response('add.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    else:
        form = hechoDeclaranteForm(request.POST)
        if form.is_valid():
            hecho = form.save(commit=False)
            hecho.declaracion_id = id
            declarante = TomaDeclaracion.objects.get(id=id)#se busca al declarante para tener el número de documento
            asociado = AsociadoDeclarante.objects.get(numero_documento_asociado=declarante.numero_documento_declarante)
            asoc = HechoAsociado(asociado_id = asociado.id,
                hecho_id = hecho.hecho_id)
            asoc.save()#cuando se guarda un hecho victimizario para un declarante se debe almacenar también para el asociado correspondiente al mismo
            #ya que siempre que se registra un declarante, el primer asociado corresponde a la misma persona
            hecho.save()#se almacena el hecho victimizario del declarante
            informacion = "Guardado"
            return render_to_response(
                'volver_declarante.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función realiza una consulta en la base de datos a partir de un identificador para determinar el registro seleccionado,
una vez encontrado se procede a eliminar."""
def delete_hecho_declarante(request, idhec, id):
    hecho = HechoDeclarante.objects.get(id=idhec)
    informacion = 'Procesando'
    if request.method == 'GET':
        hecho.delete()
        informacion = 'Eliminado'
    return render_to_response(
        'volver_declarante.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función captura un registro de la entidad seleccionado para ser modificado a partir de su identificador, presenta
un formulario estructurado a partir del modelo correspondiente con los campos presentados en el registro y permite hacer
cambios para luego ser almacenados en la base de datos."""
def update_hecho_declarante(request, idhec, id):
    hecho = HechoDeclarante.objects.get(id=idhec)
    informacion = "Procesando"
    titulo="Actualizar datos del hecho victimizario"
    if request.method == 'GET':
        form = hechoDeclaranteForm(instance=hecho)
    else:
        form = hechoDeclaranteForm(request.POST, instance=hecho)
        if form.is_valid():
            form.save()
            informacion = "Guardado"
            return render_to_response(
                'volver_declarante.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_hecho_asociado(request, id):
    informacion = "inicializando"
    titulo="Nuevo hecho victimizario"
    if request.method == 'GET':
        form = hechoAsociadoForm()
        ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add.html', 
            ctx,
            context_instance=RequestContext(request)
        )
    else:
        form = hechoAsociadoForm(request.POST)
        if form.is_valid():
            hecho = form.save(commit=False)
            hecho.asociado_id = id
            hecho.save()#se almacena el hecho victimizario del declarante
            informacion = "Guardado"
            return render_to_response(
                'volver_asociado.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función realiza una consulta en la base de datos a partir de un identificador para determinar el registro seleccionado,
una vez encontrado se procede a eliminar."""
def delete_hecho_asociado(request, idhec, id):
    hecho = HechoAsociado.objects.get(id=idhec)
    informacion = 'Procesando'
    if request.method == 'GET':
        hecho.delete()
        informacion = 'Eliminado'
    return render_to_response(
        'volver_asociado.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función captura un registro de la entidad seleccionado para ser modificado a partir de su identificador, presenta
un formulario estructurado a partir del modelo correspondiente con los campos presentados en el registro y permite hacer
cambios para luego ser almacenados en la base de datos."""
def update_hecho_asociado(request, idhec, id):
    hecho = HechoAsociado.objects.get(id=idhec)
    informacion = "Procesando"
    titulo="Actualizar datos de la etnia"
    if request.method == 'GET':
        form = hechoAsociadoForm(instance=hecho)
    else:
        form = hechoAsociadoForm(request.POST, instance=hecho)
        if form.is_valid():
            form.save()
            informacion = "Guardado"
            return render_to_response(
                'volver_asociado.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_informacion_solicitante(request):
    #panel de preguntas y respuestas para generar un capcha de verificación a fin de controlar el acceso de robots
    preguntas = ["¿Cuanto da tres por cuatro?",
    "Si a 5 le resto 2, ¿cual es la respuesta?",
    "¿Cual es la capital de Colombia?",
    "si a 4 le adiciono 5 ¿cual es el resultado?",
    "¿Cual es el resultado de dividir veinte entre cinco?",
    'Completa la frase: "El perro es el mejor amigo del ..."']
    respuestas = ["doce","3", "Bogotá", "9", "cuatro", "hombre"]

    aleatorio = random.randint(0, 5)#elige una pregunta y su respuesta al azar
    preg = preguntas[aleatorio]
    resp=respuestas[aleatorio]
    informacion = "inicializando"
    titulo="Datos básicos del solicitante"
    sistema = InformacionSolicitante.objects.get(id=0)#se obtiene el registro cero para comprobar si se están aceptando solicitudes
    estado = sistema.descripcion#corresponde al estado actual del sistema de registro de solicitudes por parte de los usuarios
    if request.method == 'GET':
        form = addInformacionSolicitanteForm()
        return render_to_response('add_usuario.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    else:
        form = addInformacionSolicitanteForm(request.POST)
        if form.is_valid():
            solic = form.save(commit=False)
            solic.estado_revision = "Pendiente"
            solic.save()
            informacion = "Guardado"
        else:
            informacion = "Error"
        return render_to_response(
            'add_usuario.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    return render_to_response('add_usuario.html', 
        locals(),
        context_instance=RequestContext(request)
    )


"""La función captura un registro de la entidad seleccionado para ser modificado a partir de su identificador, presenta
un formulario estructurado a partir del modelo correspondiente con los campos presentados en el registro y permite hacer
cambios para luego ser almacenados en la base de datos."""
def update_informacion_solicitante(request, id):
    solicitante = InformacionSolicitante.objects.get(id=id)
    informacion = "Procesando"
    titulo="Actualizar datos del solicitante"
    if request.method == 'GET':
        form = informacionSolicitanteForm(instance=solicitante)
    else:
        form = informacionSolicitanteForm(request.POST, instance=solicitante)
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


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_intermediario(request):
    informacion = "inicializando"
    titulo="Nuevo intermediario"
    if request.method == 'GET':
        form = intermediarioForm()
        ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add.html', 
            ctx,
            context_instance=RequestContext(request)
        )
    else:
        form = intermediarioForm(request.POST)
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


"""La función captura un registro de la entidad seleccionado para ser modificado a partir de su identificador, presenta
un formulario estructurado a partir del modelo correspondiente con los campos presentados en el registro y permite hacer
cambios para luego ser almacenados en la base de datos."""
def update_intermediario(request, id):
    intermediario = Intermediario.objects.get(id=id)
    informacion = "Procesando"
    titulo="Actualizar datos del intermediario"
    if request.method == 'GET':
        form = intermediarioForm(instance=intermediario)
    else:
        form = intermediarioForm(request.POST, instance=intermediario)
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


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_tipo_intermediario(request):
    informacion = "inicializando"
    titulo="Nuevo tipo de intermediario"    
    if request.method == 'GET':
        form = tipoIntermediarioForm()
        ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add.html', 
            ctx,
            context_instance=RequestContext(request)
        )
    else:
        form = tipoIntermediarioForm(request.POST)
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