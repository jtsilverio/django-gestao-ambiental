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
            "id_localidade",
            "fonte",
            "consumo",
        ]
        labels = {
            "id_localidade": "Localidade",
            "dt_agua": "Data",
            "fonte": "Fonte",
            "consumo": "Consumo (m³)",
        }
        widgets = {
            "id_localidade": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Localidade",
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
