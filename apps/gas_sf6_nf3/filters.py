import django_filters
from django.forms import Select

from apps.cluster.models import Cluster
from apps.gas_sf6_nf3.models import GasSF6NF3

# id = models.AutoField(primary_key=True)
# data = models.DateField(blank=False, null=False)
# id_cluster = models.ForeignKey(
#     Cluster, on_delete=models.PROTECT, blank=False, null=False
# )
# tp_gas = models.CharField(max_length=10, blank=False, null=False, choices=TIPO_GAS_CHOICES)
# tp_cadastro = models.CharField(max_length=10, blank=False, null=False, choices=TIPO_CADASTRO_CHOICES)
# quantidade = models.IntegerField(blank=False, null=False, default=0)


class GasSF6NF3Filter(django_filters.FilterSet):
    id_cluster = django_filters.ModelChoiceFilter(
        queryset=Cluster.objects.all(),
        label="Cluster",
        widget=Select(attrs={"class": "form-select"}),
    )

    tp_cadastro = django_filters.ChoiceFilter(
        label="Tipo de Cadastro",
        widget=Select(attrs={"class": "form-select"}),
        choices=GasSF6NF3.TIPO_CADASTRO_CHOICES,
    )

    tp_gas = django_filters.ChoiceFilter(
        label="Tipo de Gás",
        widget=Select(attrs={"class": "form-select"}),
        choices=GasSF6NF3.TIPO_GAS_CHOICES,
    )

    class Meta:
        model = GasSF6NF3  # replace with your actual model
        fields = {
            "id_cluster": [
                "exact"
            ],  # replace 'exact' with the lookup type you want to use
            "tp_cadastro": ["exact"],
            "tp_gas": ["exact"],
        }
