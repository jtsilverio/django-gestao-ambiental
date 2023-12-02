from django.forms import (
    CheckboxSelectMultiple,
    ModelForm,
    ModelMultipleChoiceField,
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

        fields = ["nome", "destinacao"]
        labels = {
            "nome": "Nome",
            "cidade": "Cidade",
            "destinacao": "Destinação",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome do Fornecedor",
                },
            ),
        }
