from django import forms

from apps.fornecedor.models import Fornecedor
from apps.saida.models import Saida


class SaidaForm(forms.ModelForm):
    id_fornecedor_destinacao = forms.ModelChoiceField(
        label="Destinadora",
        queryset=Fornecedor.objects.filter(id_tp_fornecedor__nome="DFR"),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    id_fornecedor_transporte = forms.ModelChoiceField(
        label="Transportadora",
        queryset=Fornecedor.objects.filter(id_tp_fornecedor__nome="TR"),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Saida

        fields = [
            "data",
            "id_cluster",
            "id_tp_residuos",
            "id_fornecedor_destinacao",
            "id_destinacao",
            "id_fornecedor_transporte",
            "peso",
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
            "id_fornecedor_destinacao": "Fornecedor Destinação",
            "id_destinacao": "Destinação",
            "id_fornecedor_transporte": "Fornecedor Transporte",
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
            "id_fornecedor_destinacao": forms.Select(
                attrs={"class": "form-select", "placeholder": "Fornecedor Destinação"}
            ),
            "id_destinacao": forms.Select(
                attrs={"class": "form-select", "placeholder": "Destinação"}
            ),
            "id_fornecedor_transporte": forms.Select(
                attrs={"class": "form-select", "placeholder": "Fornecedor Transporte"}
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
