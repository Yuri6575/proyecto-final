from django.db import models

class Cita(models.Model):
    paciente = models.CharField()
    medico = models.CharField()
    fecha = models.DateField()
    tipo_consulta = models.CharField()

    def __str__(self):
        return self.paciente
    