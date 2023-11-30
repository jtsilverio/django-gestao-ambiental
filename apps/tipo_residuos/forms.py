from django.forms import ModelForm, Select, TextInput

from apps.tipo_residuos.models import TipoResiduos


class TipoResiduosForm(ModelForm):
    class Meta:
        model = TipoResiduos

        fields = ["nome", "classe", "unidade_medida"]

        labels = {
            "nome": "Nome",
            "classe": "Classe",
            "unidade_medida": "Unidade de Medida",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome do Tipo de Resíduo",
                },
            ),
            "classe": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Classe do Tipo de Resíduo",
                },
            ),
            "unidade_medida": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Unidade de Medida do Tipo de Resíduo",
                },
            ),
        }
