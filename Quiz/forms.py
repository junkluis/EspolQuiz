from django import forms
from .models import Pregunta, Quiz

class preguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = ('tipo','titulo','tiempo','opCorrecta','op1','op2','op3',)

class pinForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ('pin',)
