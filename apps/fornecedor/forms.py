from django.forms import (
    CheckboxSelectMultiple,
    ModelForm,
    ModelMultipleChoiceField,
    Select,
    TextInput,
)

from apps.destinacao.models import Destinacao
from apps.fornecedor.models import Fornecedor


class FornecedorForm(ModelForm):
    destinacao = ModelMultipleChoiceField(
        label="Destinação",
        queryset=Destinacao.objects.all(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input mb-0"}),
        required=False,
    )

    class Meta:
        model = Fornecedor

        fields = ["nome", "estado", "id_cidade", "destinacao"]
        labels = {
            "nome": "Nome",
            "estado": "Estado",
            "id_cidade": "Cidade",
            "destinacao": "Destinação",
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
