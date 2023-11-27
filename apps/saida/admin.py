from django.contrib import admin

from .models import Saida


class SaidaAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id_tp_residuos",
        "id_cluster",
        "id_destinacao",
        "data",
        "peso",
        "receita",
        "custo",
        "n_evidencia",
        "cdf",
    ]
    list_filter = [
        "id_tp_residuos",
        "id_cluster",
        "id_destinacao",
        "data",
    ]
    search_fields = [
        "id_tp_residuos__nome",
        "id_cluster__nome",
        "id_destinacao__nome",
        "data",
    ]
    list_per_page = 15


admin.site.register(Saida, SaidaAdmin)
