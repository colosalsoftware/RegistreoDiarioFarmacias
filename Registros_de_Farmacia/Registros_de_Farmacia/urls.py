"""
URL configuration for Registros_de_Farmacia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home,name='home'),
    path('HumedadTemperatura/',views.registros_humedad_temperatura,name='registros'),
    path('actas/', views.lista_actas, name='lista_actas'),
    path('actas/<int:acta_id>/', views.detalle_acta, name='detalle_acta'),
    path('actas/buscar_acta/', views.buscar_acta, name='buscar_acta'),
    path('medicamento-autocomplete/', views.MedicamentoAutocomplete.as_view(), name='medicamento-autocomplete'),
    path('laboratorio-autocomplete/', views.LaboratorioAutocomplete.as_view(), name='laboratorio-autocomplete'),
    path('deposito-autocomplete/', views.DepositoAutocomplete.as_view(), name='deposito-autocomplete')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
