from django.forms import ModelForm, Select, TextInput

from apps.cluster.models import Cluster


class ClusterForm(ModelForm):
    class Meta:
        model = Cluster

        fields = ["nome", "estado", "id_cidade"]

        labels = {
            "nome": "Nome",
            "estado": "Estado",
            "id_cidade": "Cidade",
        }

        widgets = {
            "nome": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome do Cluster",
                },
            ),
            "estado": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Estado",
                },
            ),
            "id_cidade": Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Cidade",
                },
            ),
        }
