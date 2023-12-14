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

        fields = ["nome", "estado", "cidade", "destinacao"]
        labels = {
            "nome": "Nome",
            "estado": "Estado",
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
            "estado": Select(
                attrs={
                    "class": "form-select",
                },
            ),
            "cidade": Select(
                attrs={
                    "class": "form-select",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cidade"].choices = ""
        self.fields["cidade"].widget.attrs["disabled"] = True
