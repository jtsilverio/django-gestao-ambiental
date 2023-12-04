import django_filters
from django.forms import (
    CheckboxSelectMultiple,
    DateInput,
)

from apps.cluster.models import Cluster
from apps.tipo_residuos.models import TipoResiduos


class EntradaFilter(django_filters.FilterSet):
    data = django_filters.DateFilter(
        label="Data de Entrada",
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "style": "max-width: 200px;",
            }
        ),
    )
    id_tp_residuos = django_filters.ModelMultipleChoiceFilter(
        label="Tipo de Resíduo",
        queryset=TipoResiduos.objects.all(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
    )
    id_cluster = django_filters.ModelMultipleChoiceFilter(
        label="Cluster",
        queryset=Cluster.objects.all(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
    )
