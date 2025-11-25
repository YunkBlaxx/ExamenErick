from django.db import models
#se usa el archivo de modelos para 
#agregar el formulario
class DatosFormulario(models.Model):
    OPCIONES_GENERO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    OPCIONES_INTERES = [
        ('tec', 'Tecnología'),
        ('dep', 'Deportes'),
        ('art', 'Arte'),
        ('cie', 'Ciencia'),
        ('mus', 'Música'),
    ]
    
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    genero = models.CharField(max_length=1, choices=OPCIONES_GENERO)
    intereses = models.CharField(max_length=3, choices=OPCIONES_INTERES)
    edad = models.IntegerField()
    acepta_terminos = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"