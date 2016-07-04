from django.conf.urls import url

from Quiz.views import *
from . import views

app_name = 'Quiz'

urlpatterns = [

    url(r'^$',Home , name='Home'),
    url(r'^crearQuiz$',crearQuiz , name='CrearQuiz'),
    url(r'^crearQuiz/(?P<pk_quiz>[0-9]+)/$',QuizStart , name='Quiz'),
    url(r'^crearQuiz/(?P<pk_quiz>[0-9]+)/agregarPreg/$',crearPregunta , name='Quiz'),
    url(r'^crearQuiz/(?P<pk_quiz>[0-9]+)/EmpiezaJuego/$',cargarHosting , name='cargarHosting'),
    url(r'^Iniciar$',IngresarPin , name='IngresarPin'),
    #url(r'^Iniciar/(?P<pk_quiz>[0-9]+)$',IngresarU , name='IngresarPin'),
    url(r'^jugadores$', cargarUsuario, name='cargarUsuario'),
    url(r'^jugador/postUsuario', postUsuario, name='postUsuario'),
    url(r'^posthostingelementos', postHosting, name='postHosting'),

    #url(r'^crearQuiz/(?P<pk_quiz>[0-9]+)/$', agregarPreguntas, name='agregarPreguntas'),
    #url(r'^jugador$', cargarUsuario, name='cargarUsuario'),
    #url(r'^jugador/postUsuario', postUsuario, name='postUsuario'),

    #url(r'^hosting/posthostingelementos', postHosting, name='postHosting'),
    #url(r'^home', Home, name='Home'),
    #url(r'^hosting/InicioSesion', views.ingresoUser.as_view(), name='InicioSesion'),
    #url(r'^hosting/Registro', views.RegistraUsuario.as_view(), name='Registro'),
    #url(r'^hosting/cuenta', Cuenta, name='cuenta'),
]
