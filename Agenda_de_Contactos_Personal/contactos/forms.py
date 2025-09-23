from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion']
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Nombre completo',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Número de teléfono',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Correo electrónico',
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-emerald-500',
                'placeholder': 'Dirección',
            }),
        }
