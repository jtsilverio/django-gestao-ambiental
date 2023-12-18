from django.forms import (
    CheckboxSelectMultiple,
    ModelForm,
    ModelMultipleChoiceField,
    Select,
    TextInput,
)

from apps.destinacao.models import Destinacao
from apps.fornecedor.models import Fornecedor, TipoFornecedor


class FornecedorForm(ModelForm):
    id_destinacao = ModelMultipleChoiceField(
        label="Destinação",
        queryset=Destinacao.objects.all(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input mb-0"}),
        required=False,
    )

    id_tp_fornecedor = ModelMultipleChoiceField(
        label="Tipo de Fornecedor",
        queryset=TipoFornecedor.objects.all(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input mb-0"}),
        required=False,
    )

    class Meta:
        model = Fornecedor

        fields = ["nome", "id_tp_fornecedor", "estado", "id_cidade", "id_destinacao"]
        labels = {
            "nome": "Nome",
            "id_tp_fornecedor": "Tipo de Fornecedor",
            "estado": "Estado",
            "id_cidade": "Cidade",
            "id_destinacao": "Destinação",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome do Fornecedor",
                },
            ),
            "estado": Select(
                attrs={
                    "class": "form-select",
                },
            ),
            "id_cidade": Select(
                attrs={
                    "class": "form-select",
                },
            ),
        }
