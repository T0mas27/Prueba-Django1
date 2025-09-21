from django.shortcuts import render, redirect
from .models import Contacto
from .forms import ContactoForm
from django.db.models import Q

def lista_contactos(request):
    query = request.GET.get('q')
    if query:
        contactos = Contacto.objects.filter(Q(nombre__icontains=query) | Q(correo__icontains=query))
    else:
        contactos = Contacto.objects.all()
    return render(request, 'contactos/lista_contactos.html', {'contactos': contactos})

def agregar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'contactos/agregar_contacto.html', {'form': form})
