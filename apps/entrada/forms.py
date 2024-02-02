from django.forms import CharField, DateInput, ModelForm, NumberInput, Select, TextInput

from apps.entrada.models import Entrada


class EntradaForm(ModelForm):
    classe_residuo = CharField(
        required=False,
        label="Classe",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
                "disabled": "disabled",
            }
        ),
    )

    unidade_medida = CharField(
        required=False,
        label="Unid. de Medida",
        widget=TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
                "disabled": "disabled",
            }
        ),
    )

    class Meta:
        model = Entrada

        fields = [
            "data",
            "id_cluster",
            "id_tp_residuos",
            "classe_residuo",
            "quantidade",
            "unidade_medida",
        ]

        labels = {
            "data": "Data de Entrada",
            "id_cluster": "Cluster",
            "id_tp_residuos": "Tipo de Resíduo",
            "quantidade": "Quantidade",
            "unidade_medida": "Unidade de Medida",
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
            "quantidade": NumberInput(
                attrs={"class": "form-control"},
            ),
        }
