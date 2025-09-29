from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm
from django.db.models import Q

def lista_contactos(request):
    """
    Vista para mostrar la lista de contactos.
    Permite buscar contactos por nombre o correo usando el parámetro 'q' en GET.
    """
    query = request.GET.get('q')  #Obtener término de buscar
    if query:
        # Filtra contactos que contengan el término en nombre o correo
        contactos = Contacto.objects.filter(Q(nombre__icontains=query) | Q(correo__icontains=query))
    else:
        # Si no hay búsqueda muestra todos los contactos
        contactos = Contacto.objects.all()
    
    # Renderizar la plantilla con la lista de contactos
    return render(request, 'contactos/lista_contactos.html', {'contactos': contactos})


def agregar_contacto(request):
    """
    Vista para agregar un nuevo contacto.
    Muestra un formulario vacío y procesa el formulario cuando se envía (POST).
    """
    if request.method == 'POST':
        form = ContactoForm(request.POST)  # Crea formulario con datos enviados
        if form.is_valid():
            form.save()  # Guardar nuevo contacto en la base de datos
            return redirect('lista_contactos')  # Redirigir a la lista de contactos
    else:
        form = ContactoForm()  # Crear formulario vacío para mostrar
    
    # Renderizar la pagina con el formulario
    return render(request, 'contactos/agregar_contacto.html', {'form': form})


def editar_contacto(request, id):
    """
    Vista para editar un contacto existente identificado por su 'id'.
    Si el método es GET, muestra el formulario con los datos actuales del contacto.
    Si es POST, valida y guarda los cambios.
    """
    # Obtener el contacto o devolver error 404 si no existe
    contacto = get_object_or_404(Contacto, id=id)

    if request.method == 'POST':
        # Crear formulario con datos enviados y la instancia para actualizar
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()  # Guardar los cambios en la base de datos
            return redirect('lista_contactos')  # Volver a la lista de contactos
    else:
        # muestra el formulario con los datos actuales del contacto
        form = ContactoForm(instance=contacto)

    # Renderizar la misma plantilla que agregar, pero pasando el contacto para indicar edición
    return render(request, 'contactos/agregar_contacto.html', {'form': form, 'contacto': contacto})


def borrar_contacto(request, id):
    """
    Vista para borrar un contacto identificado por su 'id'.
    Solo acepta solicitudes POST para evitar borrados accidentales.
    Después de borrar, redirige a la lista de contactos.
    """
    contacto = get_object_or_404(Contacto, id=id)

    if request.method == 'POST':
        contacto.delete()  # Borrar el contacto de la base de datos
        return redirect('lista_contactos')

    # Si la solicitud no es POST, redirige igual a la lista 
    return redirect('lista_contactos')
