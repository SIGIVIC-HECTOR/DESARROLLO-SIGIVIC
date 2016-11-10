# -*- coding: 850 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from beneficios.models import *
from beneficios.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


"""La función hace una captura de la entidad BeneficioVictima de la base de datos y presenta todos sus registros
en una lista paginada."""
def lista_beneficios(request):
    beneficios = BeneficioVictima.objects.all()
    paginator = Paginator(beneficios, 10) # muestra 10 contactos por página

    page = request.GET.get('page')
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    return render_to_response(
        'lista_beneficios.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


"""La función agrega un nuevo registro a la entidad de la base de datos correspondiente, el proceso de validación se hace
mediante un formulario estructurado a partir de la misma entidad de la base de datos."""
def add_beneficio(request):
    informacion = "inicializando"
    titulo="Nuevo beneficio"
    if request.method == 'GET':
        form = beneficioVictimaForm()
        ctx = {'form':form, 'informacion':informacion, 'titulo': titulo}
        return render_to_response('add.html', 
            ctx,
            context_instance=RequestContext(request)
        )
    else:
        form = beneficioVictimaForm(request.POST)
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


"""La función obtiene un registro de la entidad correspondiente de la base de datos a partir de su id, hace uso
de un formulario estructurado a partir de la misma entidad y actualiza los datos en el mismo registro consultado."""
def update_beneficio(request, id):
    beneficio = BeneficioVictima.objects.get(id=id)
    informacion = "Procesando"
    titulo="Actualizar datos del beneficio"
    if request.method == 'GET':
        form = beneficioVictimaForm(instance=beneficio)
    else:
        form = beneficioVictimaForm(request.POST, instance=beneficio)
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