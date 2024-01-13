from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import OuterRef, Subquery
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.entrada.filters import EntradaFilter as ModelFilter
from apps.entrada.forms import EntradaForm as ModelForm
from apps.entrada.models import Entrada as Model
from apps.tipo_residuos.models import TipoResiduos
from apps.utils import (
    create_filtered_context,
    paginate_query,
)

APP_NAME = "entrada"
APP_TITLE = "Entrada"


def index(request):
    model_filter = ModelFilter(request.GET, queryset=Model.objects.all())
    referenced_tp_residuos = TipoResiduos.objects.filter(
        id__in=model_filter.qs.values("id_tp_residuos")
    )

    # Create a subquery that gets 'classe' from referenced_tp_residuos
    classe_subquery = referenced_tp_residuos.filter(
        id=OuterRef("id_tp_residuos")
    ).values("classe")[:1]

    # Annotate the queryset with the subquery
    annotated_qs = model_filter.qs.annotate(classe=Subquery(classe_subquery))

    # paginate the queryset
    query_filtered = paginate_query(request, annotated_qs, settings.PAGESIZE)

    # create the context with additinal info as the number of active filters, app name and title
    context = create_filtered_context(query_filtered, model_filter, request)
    context["title"] = APP_TITLE
    context["app_name"] = APP_NAME

    return render(request, f"{APP_NAME}/index.html", context)


class Create(SuccessMessageMixin, CreateView):
    model = Model
    form_class = ModelForm
    template_name = f"{APP_NAME}/create.html"
    success_message = f"{APP_TITLE} Cadastrado"
    extra_context = {"title": APP_TITLE, "app_name": APP_NAME}
    success_url = reverse_lazy(f"{APP_NAME}:index")

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response


class Edit(SuccessMessageMixin, UpdateView):
    model = Model
    form_class = ModelForm
    template_name = f"{APP_NAME}/edit.html"
    success_message = f"{APP_TITLE} Atualizado"
    extra_context = {"title": APP_TITLE, "app_name": APP_NAME}
    success_url = reverse_lazy(f"{APP_NAME}:index")


def delete(request, pk):
    entry = get_object_or_404(Model, pk=pk)

    if request.method == "POST":
        entry.delete()
        messages.warning(request, f"{APP_TITLE} Excluído")

    return redirect(f"{APP_NAME}:index")
