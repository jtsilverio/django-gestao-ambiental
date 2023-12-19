from apps.cidades.models import Cidades


class EmptyCidadeMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "id_cidade" in self.fields:
            self.fields["id_cidade"].queryset = Cidades.objects.none()
            self.fields["id_cidade"].disabled = True
