import django.forms as forms

from apps.cidades.models import Cidades


class EmptyCidadeMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "id_cidade" in self.fields and not self.is_bound:
            self.fields["id_cidade"].empty_label = "Selecione um Estado"
            self.fields["id_cidade"].disabled = True
            self.fields["id_cidade"].queryset = Cidades.objects.none()

    def clean_id_cidade(self):
        id_cidade = self.cleaned_data.get("id_cidade")
        if not Cidades.objects.filter(id=id_cidade.id).exists():
            raise forms.ValidationError("Cidade Inválida")

        return id_cidade
