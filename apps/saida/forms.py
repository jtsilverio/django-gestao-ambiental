from django import forms

from apps.fornecedor.models import Fornecedor
from apps.saida.models import Saida


class SaidaForm(forms.ModelForm):
    id_fornecedor_destinacao = forms.ModelChoiceField(
        label="Destinadora",
        queryset=Fornecedor.objects.filter(id_tp_fornecedor__nome="Destinação Final"),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    id_fornecedor_transporte = forms.ModelChoiceField(
        label="Transportadora",
        queryset=Fornecedor.objects.filter(id_tp_fornecedor__nome="Transporte"),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    classe_residuo = forms.CharField(
        required=False,
        label="Classe",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
                "disabled": "disabled",
            }
        ),
    )

    unidade_medida = forms.CharField(
        required=False,
        label="Unid. de Medida",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
                "disabled": "disabled",
            }
        ),
    )

    class Meta:
        model = Saida

        fields = [
            "data",
            "id_cluster",
            "id_tp_residuos",
            "classe_residuo",
            "id_fornecedor_destinacao",
            "id_destinacao",
            "id_fornecedor_transporte",
            "quantidade",
            "unidade_medida",
            "receita",
            "custo",
            "cdf",
            "evidencia",
        ]

        labels = {
            "data": "Data de Saída",
            "id_cluster": "Cluster",
            "id_tp_residuos": "Tipo de Resíduo",
            "classe_residuo": "Classe",
            "quantidade": "Quantidade",
            "unidade_medida": "Unidade de Medida",
            "id_fornecedor_destinacao": "Fornecedor Destinação",
            "id_destinacao": "Destinação",
            "id_fornecedor_transporte": "Fornecedor Transporte",
            "receita": "Receita",
            "custo": "Custo",
            "cdf": "CDF",
            "evidencia": "Evidência",
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
            "quantidade": forms.NumberInput(
                attrs={"class": "form-control"},
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
            "cdf": forms.FileInput(
                attrs={"class": "form-control"},
            ),
            "evidencia": forms.FileInput(
                attrs={"class": "form-control"},
            ),
        }
