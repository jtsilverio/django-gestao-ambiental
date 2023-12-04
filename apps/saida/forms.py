from django import forms

from apps.fornecedor.models import Fornecedor
from apps.saida.models import Saida


class SaidaForm(forms.ModelForm):
    id_fornecedor = forms.ModelChoiceField(
        label="Fornecedor",
        queryset=Fornecedor.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Saida

        fields = [
            "data",
            "id_cluster",
            "id_tp_residuos",
            "peso",
            "id_fornecedor",
            "id_destinacao",
            "receita",
            "custo",
            "n_evidencia",
            "cdf",
        ]

        labels = {
            "data": "Data de Saída",
            "id_cluster": "Cluster",
            "id_tp_residuos": "Tipo de Resíduo",
            "peso": "Peso",
            "id_fornecedor": "Fornecedor",
            "id_destinacao": "Destinação",
            "receita": "Receita",
            "custo": "Custo",
            "n_evidencia": "Nº Evidência",
            "cdf": "CDF",
        }

        widgets = {
            "data": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
            "id_cluster": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Cluster",
                }
            ),
            "id_tp_residuos": forms.Select(
                attrs={"class": "form-select", "placeholder": "Tipo Resíduo"}
            ),
            "peso": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Localidade"},
            ),
            "id_fornecedor": forms.Select(
                attrs={"class": "form-select", "placeholder": "Fornecedor"}
            ),
            "id_destinacao": forms.Select(
                attrs={"class": "form-select", "placeholder": "Destinação"}
            ),
            "receita": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Receita"},
            ),
            "custo": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Custo"},
            ),
            "n_evidencia": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nº Evidência"},
            ),
            "cdf": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "CDF"},
            ),
        }
