from rest_framework import serializers
from .models import cita

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = cita
        fields = ['id','paciente','medico','fecha','tipo_consulta']