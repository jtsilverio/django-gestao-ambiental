import django_filters
from django.forms import (
    CheckboxInput,
    CheckboxSelectMultiple,
    DateInput,
    Select,
)

from apps.cluster.models import Cluster
from apps.fornecedor.models import Destinacao, Fornecedor
from apps.tipo_residuos.models import TipoResiduos


class SaidaFilter(django_filters.FilterSet):
    data = django_filters.DateFilter(
        label="Data de Saida",
        widget=DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "style": "max-width: 200px;",
            }
        ),
    )
    id_fornecedor = django_filters.ModelChoiceFilter(
        label="Fornecedor",
        queryset=Fornecedor.objects.all(),
        widget=Select(attrs={"class": "form-select"}),
    )

    id_destinacao = django_filters.ModelChoiceFilter(
        label="Destinação",
        queryset=Destinacao.objects.all(),
        widget=Select(attrs={"class": "form-select"}),
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

    cdf = django_filters.BooleanFilter(
        label="CDF Vazio",
        field_name="cdf",
        lookup_expr="isnull",
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
        method="filter_cdf",
    )

    def filter_cdf(self, queryset, name, value):
        if value:
            # Show only empty CDF
            queryset = queryset.filter(**{f"{name}__exact": ""})
        return queryset
