from random import randint
from .forms import preguntaForm, pinForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect

from .models import *

# Create your views here.
def Home(request):  #HomePage de la aplicaciones
    return render(request, 'home.html')

def crearPregunta(request, pk_quiz):
    form = preguntaForm()
    if request.method == 'POST':
        form = preguntaForm(request.POST)
        if form.is_valid():
            preg = form.save(commit=False)
            preg.tipo = form.cleaned_data['tipo']
            preg.titulo = form.cleaned_data['titulo']
            preg.tiempo = form.cleaned_data['tiempo']
            preg.opCorrecta = form.cleaned_data['opCorrecta']
            preg.op1 = form.cleaned_data['op1']
            preg.op2 = form.cleaned_data['op2']
            preg.op3 = form.cleaned_data['op3']
            preg.quiz = Quiz.objects.get(id=pk_quiz)
            preg.save()

            return HttpResponseRedirect('/crearQuiz/'+str(pk_quiz)+'/')

        else:
            form = preguntaForm()
    return render(request, 'addPregunta.html', {'form': form, 'request':request})


def QuizStart(request, pk_quiz):
    quiz = Quiz.objects.get(id = pk_quiz)
    return render(request, 'Quiz.html',{'quiz':quiz})



def crearQuiz(request):
    if request.method == 'POST':
        aleatorio = generarPinAleatorio()
        quiz = Quiz()
        quiz.pin = aleatorio
        quiz.save()
        return redirect('crearQuiz/'+str(quiz.pk)+'/')
    else:
        return render(request, 'crearQuiz.html')

def IngresarPin(request):
    form = pinForm()
    if request.method == 'POST':
        form = pinForm(request.POST)
        quizOb = Quiz()
        if form.is_valid():
            pinIn = form.cleaned_data['pin']
            try:
                quizOb = Quiz.objects.get(pin__exact=pinIn)
                return HttpResponse("<h1>"+quizOb.pin+"  pk:"+str(quizOb.pk)+"</h1>")
            except quizOb.DoesNotExist:

                return render(request, 'IngresePin.html', {'form': form,'error':'No existe el pin'})

    return render(request, 'IngresePin.html', {'form': form})





def cargarHosting(request, pk_quiz):
    return render(request, 'hosting.html')


def cargarUsuario(request):
    return render(request, 'jugadores.html')

def postUsuario(request):
    q = Quiz.objects.create(nombre=request.POST["texto"])
    # data=serializers.serialize('json',Quiz.objects.all(),fields=('nombre','descripcion'))


    return HttpResponse("se ingreso")
    """
    data=serializers.serialize('json',Quiz.objects.all(),fields=('nombre','descripcion'))
    a=json.loads(data) #coje un string (que tenga modelo de json creo) y lo transforma a objeto json
    b=json.dumps(a) #coje un objeto de tipo json y lo transforma a string
    return HttpResponse(b)
    """



def postHosting(request):
    data = serializers.serialize('json', Quiz.objects.all(), fields=('nombre', 'descripcion'))
    return HttpResponse(data, content_type="application/json")

def generarPinAleatorio():
    caracter = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    pin = ''
    for x in range(0,8):
        pin = pin + caracter[randint(0,35)]
    return pin