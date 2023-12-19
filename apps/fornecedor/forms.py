from django.forms import (
    CheckboxSelectMultiple,
    ModelForm,
    ModelMultipleChoiceField,
    Select,
    TextInput,
)

from apps.destinacao.models import Destinacao
from apps.fornecedor.models import Fornecedor, TipoFornecedor
from apps.utils.models import EmptyCidadeMixin


class FornecedorForm(EmptyCidadeMixin, ModelForm):
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

        fields = ["nome", "estado", "id_cidade", "id_tp_fornecedor", "id_destinacao"]
        labels = {
            "nome": "Nome",
            "estado": "Estado",
            "id_cidade": "Cidade",
            "id_tp_fornecedor": "Tipo de Fornecedor",
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
