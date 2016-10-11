from django.conf.urls import include, url

urlpatterns = [
    url(r'^add_beneficio/$', 'beneficios.views.add_beneficio', name='add_beneficio'),
    url(r'^lista_beneficios/$', 'beneficios.views.lista_beneficios', name='lista_beneficios'),
    url(r'^update_beneficio/(?P<id>\d+)/$', 'beneficios.views.update_beneficio', name='update_beneficio'),
]