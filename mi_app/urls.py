from django.urls import path
from . import views

app_name = 'mi_app'

urlpatterns = [
    path('', views.formulario_view, name='formulario'),
    path('exito/', views.exito_view, name='exito'),
]