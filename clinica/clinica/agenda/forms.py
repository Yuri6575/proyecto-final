from django import forms #Módulo de Django para trabajar con formularios
from .models import Cita # Importa el modelo cita desde el archivo models.py

class CitaForm(forms.ModelForm): # Define un formulario basado en el modelo cita
    class Meta:
        model = Cita
        fields = ['paciente', 'medico', 'fecha', 'tipo_consulta'] # Especifica los campos que se incluirán en el formulario
        widgets = {  #Permite personalizar cómo se renderizan los campos en HTML
            'fecha': forms.DateInput(attrs={'type': 'date'}), # Utiliza un campo de entrada de fecha HTML5
        }