from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from .forms import CitaForm
# from django.http import HttpResponse
# from reportlab.pdfgen import canvas


#Vista para listar todas las citas existentes
def lista_citas(request): 
    citas = Cita.objects.all()
    return render(request, 'agenda/lista_citas.html', {'citas': citas})

#Maneja tanto la presentación del formulario vacío (GET) - enviado (POST).
def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'agenda/crear_cita.html', {'form': form})


#Vista para editar una cita existente
def editar_cita(request, pk):
    cita_obj = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita_obj)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita_obj)
    return render(request, 'agenda/editar_cita.html', {'form': form})

def eliminar_cita(request, pk):
    cita_obj = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita_obj.delete()
        return redirect('lista_citas')
    return render(request, 'agenda/eliminar_cita.html', {'cita': cita_obj})


# def generar_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="informe.pdf"'
    
#     p = canvas.Canvas(response)
#     p.drawString(100, 100, "Hola, este es un PDF generado con ReportLab!")
#     p.showPage()
#     p.save()
    
#     return response