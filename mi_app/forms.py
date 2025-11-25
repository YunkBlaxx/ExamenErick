from django import forms
from .models import DatosFormulario
#Este archivo se crea no esta prehecho
class FormularioDatos(forms.ModelForm):
    # Campo 1: Texto normal
    nombre = forms.CharField(
        label='Nombre Completo',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre completo'
        })
    )
    
    # Campo 2: Email
    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@correo.com'
        })
    )
    
    # Campo 3: Botones de radio
    genero = forms.ChoiceField(
        label='Género',
        choices=DatosFormulario.OPCIONES_GENERO,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input'
        })
    )
    
    # Campo 4: Lista desplegable
    intereses = forms.ChoiceField(
        label='Interés Principal',
        choices=DatosFormulario.OPCIONES_INTERES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    # Campo 5: Número
    edad = forms.IntegerField(
        label='Edad',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '18',
            'max': '100'
        })
    )
    
    # Campo extra: Checkbox
    acepta_terminos = forms.BooleanField(
        label='Acepto los términos y condiciones',
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    class Meta:
        model = DatosFormulario
        fields = ['nombre', 'email', 'genero', 'intereses', 'edad', 'acepta_terminos']