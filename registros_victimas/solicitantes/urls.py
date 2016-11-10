# -*- coding: 850 -*-
from django.conf.urls import include, url

"""Cada url crea una nueva dirección en el sitio a partir de la dirección base solicitantes"""

urlpatterns = [
	url(r'^add_informacion_solicitante/$', 'solicitantes.views.add_informacion_solicitante', name='add_informacion_solicitante'),
	url(r'^add_declaracion/$', 'solicitantes.views.add_declaracion', name='add_declaracion'),
    url(r'^add_asociado_declarante/$', 'solicitantes.views.add_asociado', name='add_asociado_declarante'),
    url(r'^add_beneficio_asociado/(?P<id>\d+)/$', 'solicitantes.views.add_beneficio_asociado', name='add_beneficio_asociado'),
    url(r'^add_discapacidad_asociado/(?P<id>\d+)/$', 'solicitantes.views.add_discapacidad_asociado', name='add_discapacidad_asociado'),
    url(r'^add_etnia_asociado/(?P<id>\d+)/$', 'solicitantes.views.add_etnia_asociado', name='add_etnia_asociado'),
    url(r'^add_correccion_declaracion/$', 'solicitantes.views.add_correccion_declaracion', name='add_correccion_declaracion'),
	url(r'^add_hecho_asociado/(?P<id>\d+)/$', 'solicitantes.views.add_hecho_asociado', name='add_hecho_asociado'),
	url(r'^add_hecho_declarante/(?P<id>\d+)/$', 'solicitantes.views.add_hecho_declarante', name='add_hecho_declarante'),
    url(r'^add_informacion_solicitante/$', 'solicitantes.views.add_informacion_solicitante', name='add_informacion_solicitante'),
	url(r'^add_intermediario/$', 'solicitantes.views.add_intermediario', name='add_intermediario'),
	url(r'^add_tipo_intermediario/$', 'solicitantes.views.add_tipo_intermediario', name='add_tipo_intermediario'),
	
    url(r'^lista_declarantes/$', 'solicitantes.views.lista_declarantes', name='lista_declarantes'),
	url(r'^lista_asociados_declarante/(?P<id>\d+)/$', 'solicitantes.views.lista_asociados_declarante', name='lista_asociados_declarante'),
    url(r'^lista_solicitantes/$', 'solicitantes.views.lista_solicitantes', name='lista_solicitantes'),
	url(r'^lista_intermediarios/$', 'solicitantes.views.lista_intermediarios', name='lista_intermediarios'),
	#url(r'^update_asociado_declarante/$', 'solicitantes.views.update_asociado_declarante', name='update_asociado_declarante'),	
    url(r'^delete_beneficio_asociado/(?P<idben>\d+)/(?P<id>\d+)/$', 'solicitantes.views.delete_beneficio_asociado', name='delete_beneficio_asociado'),
    url(r'^delete_discapacidad_asociado/(?P<iddisc>\d+)/(?P<id>\d+)/$', 'solicitantes.views.delete_discapacidad_asociado', name='delete_discapacidad_asociado'),
    url(r'^delete_etnia_asociado/(?P<idet>\d+)/(?P<id>\d+)/$', 'solicitantes.views.delete_etnia_asociado', name='delete_etnia_asociado'),
    url(r'^delete_hecho_asociado/(?P<idhec>\d+)/(?P<id>\d+)/$', 'solicitantes.views.delete_hecho_asociado', name='delete_hecho_asociado'),
    url(r'^delete_hecho_declarante/(?P<idhec>\d+)/(?P<id>\d+)/$', 'solicitantes.views.delete_hecho_declarante', name='delete_hecho_declarante'),


    url(r'^update_asociado_declarante/(?P<id>\d+)/$', 'solicitantes.views.update_asociado_declarante', name='update_asociado_declarante'),
    url(r'^update_beneficio_asociado/(?P<idben>\d+)/(?P<id>\d+)/$', 'solicitantes.views.update_beneficio_asociado', name='update_beneficio_asociado'),
    url(r'^update_discapacidad_asociado/(?P<iddisc>\d+)/(?P<id>\d+)/$', 'solicitantes.views.update_discapacidad_asociado', name='update_discapacidad_asociado'),
    url(r'^update_etnia_asociado/(?P<idet>\d+)/(?P<id>\d+)/$', 'solicitantes.views.update_etnia_asociado', name='update_etnia_asociado'),
    url(r'^update_hecho_asociado/(?P<idhec>\d+)/(?P<id>\d+)/$', 'solicitantes.views.update_hecho_asociado', name='update_hecho_asociado'),
    url(r'^update_hecho_declarante/(?P<idhec>\d+)/(?P<id>\d+)/$', 'solicitantes.views.update_hecho_declarante', name='update_hecho_declarante'),
    url(r'^update_declarante/(?P<id>\d+)/$', 'solicitantes.views.update_declarante', name='update_declarante'),
    url(r'^update_informacion_solicitante/(?P<id>\d+)/$', 'solicitantes.views.update_informacion_solicitante', name='update_informacion_solicitante'),
    url(r'^update_intermediario/(?P<id>\d+)/$', 'solicitantes.views.update_intermediario', name='update_intermediario'),

    #url(r'^solicitud_view/$', 'solicitantes.views.solicitud_view', name='solicitud_view'),

]