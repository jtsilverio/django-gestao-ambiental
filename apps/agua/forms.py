from django.forms import (
    DateInput,
    ModelForm,
    NumberInput,
    Select,
)

from apps.agua.models import Agua


class AguaForm(ModelForm):
    class Meta:
        model = Agua
        fields = [
            "data",
            "id_cluster",
            "id_unidade_consumo",
            "fonte",
            "consumo",
        ]
        labels = {
            "id_cluster": "Cluster",
            "id_unidade_consumo": "Unidade de Consumo",
            "dt_agua": "Data",
            "fonte": "Fonte",
            "consumo": "Consumo (m³)",
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
            "fonte": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Fonte",
                }
            ),
            "consumo": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Consumo",
                }
            ),
        }
