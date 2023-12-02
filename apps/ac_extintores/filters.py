import django_filters
from django.forms import Select

from apps.ac_extintores.models import ACExtintores
from apps.cluster.models import Cluster


class ACExtintoresFilter(django_filters.FilterSet):
    id_cluster = django_filters.ModelChoiceFilter(
        queryset=Cluster.objects.all(),
        label="Cluster",
        widget=Select(attrs={"class": "form-select"}),
    )

    fonte_emissao = django_filters.ChoiceFilter(
        label="Fonte de Emissão",
        widget=Select(attrs={"class": "form-select"}),
        choices=ACExtintores.FONTE_EMISSAO_CHOICES,
    )

    tp_gas = django_filters.ChoiceFilter(
        label="Tipo de Gás",
        widget=Select(attrs={"class": "form-select"}),
        choices=ACExtintores.TIPO_GAS_CHOICES,
    )

    class Meta:
        model = ACExtintores  # replace with your actual model
        fields = {
            "id_cluster": [
                "exact"
            ],  # replace 'exact' with the lookup type you want to use
            "fonte_emissao": ["exact"],
            "tp_gas": ["exact"],
        }
