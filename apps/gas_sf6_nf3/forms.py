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
        # Call the parent form's initialization method
        super().__init__(*args, **kwargs)

        # Iterate over all fields of the form
        for name, field in self.fields.items():
            # If the field is a CharField or IntegerField
            if isinstance(field, (forms.CharField, forms.IntegerField)):
                # Update the field's widget attributes to add a CSS class "form-control"
                field.widget.attrs.update({"class": "form-control"})

            # If the field is a ChoiceField
            elif isinstance(field, forms.ChoiceField):
                # Update the field's widget attributes to add a CSS class "form-select"
                field.widget.attrs.update({"class": "form-select"})

            # If the field is a DateField
            elif isinstance(field, forms.DateField):
                # Change the field's widget to a DateInput widget with a CSS class "form-control"
                # and set the input type to "date"
                field.widget = forms.DateInput(
                    attrs={"type": "date", "class": "form-control"}
                )
