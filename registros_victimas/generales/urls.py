# -*- coding: 850 -*-
from django.conf.urls import include, url

"""Cada url crea una nueva dirección en el sitio a partir de la dirección base generales"""

urlpatterns = [
	url(r'^add_tipo_doc/$', 'generales.views.add_tipo_documento', name='add_tipo_documento'),
    url(r'^add_lugar_declaracion/$', 'generales.views.add_lugar_declaracion', name='add_lugar_declaracion'),
    url(r'^lista_lugares_declaracion/$', 'generales.views.lista_lugares_declaracion', name='lista_lugares_declaracion'),
    url(r'^lista_tipos_documento/$', 'generales.views.lista_tipos_documentos_generales', name='lista_tipos_documento'),
    url(r'^add_entidad_atencion/$', 'generales.views.add_entidad_atencion', name='add_entidad_atencion'),
    url(r'^matriz/$', 'generales.views.matriz', name='matriz'),
    url(r'^login_view/$', 'generales.views.login_view', name='login_view'),
    url(r'^index_view/$', 'generales.views.index_view', name='index_view'),
    url(r'^logout_view/$', 'generales.views.logout_view', name='logout_view'),
    url(r'^estado_clientes_view/$', 'generales.views.estado_clientes_view', name='estado_clientes_view'),
    url(r'^lista_notificaciones/(?P<id>\d+)/$', 'generales.views.lista_notificaciones', name='lista_notificaciones'),
    url(r'^notificaciones/$', 'generales.views.notificaciones', name='notificaciones'),
    url(r'^info/$', 'generales.views.info', name='info'),
]