from django.forms import ModelForm, TextInput

from apps.tipo_residuos.models import TipoResiduos


class TipoResiduosForm(ModelForm):
    class Meta:
        model = TipoResiduos

        fields = [
            "nome",
        ]

        labels = {
            "nome": "Nome",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome do Tipo de Resíduo",
                },
            )
        }
