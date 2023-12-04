from django import forms

from .models import GasSF6NF3


class GasSF6NF3Form(forms.ModelForm):
    class Meta:
        model = GasSF6NF3
        fields = "__all__"
        labels = {
            "id_cluster": "Cluster",
            "data": "Data",
            "tp_gas": "Tipo de Gás",
            "tp_cadastro": "Tipo de Cadastro",
            "quantidade": "Quantidade",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field, (forms.CharField, forms.IntegerField)):
                field.widget.attrs.update({"class": "form-control"})
            elif isinstance(field, forms.ChoiceField):
                field.widget.attrs.update({"class": "form-select"})
            elif isinstance(field, forms.DateField):
                field.widget = forms.DateInput(
                    attrs={"type": "date", "class": "form-control"}
                )
