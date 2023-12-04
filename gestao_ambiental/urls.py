"""Core URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path

# fmt: off
urlpatterns = [
    path("", include("apps.home.urls")),
    path("admin/", admin.site.urls),
    path("entrada/", include("apps.entrada.urls")),
    path("saida/", include("apps.saida.urls")),
    path("fornecedor/", include("apps.fornecedor.urls")),
    path("cluster/", include("apps.cluster.urls")),
    path("tipo_residuos/", include("apps.tipo_residuos.urls")),
    path("destinacao/", include("apps.destinacao.urls")),
    path("agua/", include("apps.agua.urls")),
    path("eletricidade/", include("apps.eletricidade.urls")),
    path("combustivel/", include("apps.combustivel.urls")),
    path("tipo_combustivel/", include("apps.tipo_combustivel.urls", namespace="tipo_combustivel")),
    path("unidade_consumo/", include("apps.unidade_consumo.urls", namespace="unidade_consumo")),
    path("ac_extintores/", include("apps.ac_extintores.urls", namespace="ac_extintores")),
    path("gas_sf6_nf3/", include("apps.gas_sf6_nf3.urls", namespace="gas_sf6_nf3"))
]
# fmt: on
