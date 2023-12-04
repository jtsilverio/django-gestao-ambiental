from django.forms import (
    DateInput,
    ModelForm,
    NumberInput,
    Select,
)

from apps.eletricidade.models import Eletricidade


class EletricidadeForm(ModelForm):
    class Meta:
        model = Eletricidade
        fields = [
            "data",
            "id_cluster",
            "id_unidade_consumo",
            "consumo",
        ]
        labels = {
            "data": "Data",
            "id_cluster": "Cluster",
            "id_unidade_consumo": "Unidade de Consumo",
            "consumo": "Consumo (kWh)",
        }
        widgets = {
            "id_cluster": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Cluster",
                }
            ),
            "id_unidade_consumo": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Unidade de Consumo",
                }
            ),
            "data": DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Data",
                    "type": "date",
                }
            ),
            "consumo": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Consumo",
                }
            ),
        }
