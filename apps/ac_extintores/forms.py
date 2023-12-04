from django import forms

from .models import ACExtintores


class ACExtintoresForm(forms.ModelForm):
    class Meta:
        model = ACExtintores
        fields = "__all__"
        labels = {
            "id_cluster": "Cluster",
            "data": "Data",
            "fonte_emissao": "F. Emissão",
            "tp_gas": "Tipo de Gás",
            "n_unidades": "N. Unidades",
            "tp_cadastro": "Cadastro",
            "carga": "Carga",
            "capacidade": "Capacidade",
            "recuperacao": "Recuperação",
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
