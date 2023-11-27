from django.forms import DateInput, ModelForm, NumberInput, Select

from apps.entrada.models import Entrada


class EntradaForm(ModelForm):
    class Meta:
        model = Entrada

        fields = [
            "data",
            "id_cluster",
            "id_tp_residuos",
            "peso",
        ]

        labels = {
            "data": "Data de Entrada",
            "id_cluster": "Cluster",
            "id_tp_residuos": "Tipo de Resíduo",
            "peso": "Peso",
        }

        widgets = {
            "data": DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
            "id_cluster": Select(
                attrs={"class": "form-select", "placeholder": "Localidade"}
            ),
            "id_tp_residuos": Select(
                attrs={"class": "form-select", "placeholder": "Tipo Resíduo"}
            ),
            "peso": NumberInput(
                attrs={"class": "form-control", "placeholder": "Localidade"},
            ),
        }
