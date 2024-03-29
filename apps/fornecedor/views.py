from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.fornecedor.filters import FornecedorFilter as ModelFilter
from apps.fornecedor.forms import FornecedorForm as ModelForm
from apps.fornecedor.models import Fornecedor as Model
from apps.utils import (
    create_filtered_context,
    paginate_query,
)

APP_NAME = "fornecedor"
APP_TITLE = "Fornecedor"


def index(request):
    model_filter = ModelFilter(request.GET, queryset=Model.objects.all())

    query_filtered = paginate_query(request, model_filter.qs, settings.PAGESIZE)
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


def get_destinacao(request):
    id_fornecedor = request.GET.get("id")
    fornecedor = get_object_or_404(Model, pk=id_fornecedor)

    id_destinacao = (
        fornecedor.id_destinacao.all()
    )  # get the queryset of the ManyToMany field
    id_destinacao = serializers.serialize("json", id_destinacao)

    # JsonResponse will automatically convert the serialized data to a JSON response
    return JsonResponse(id_destinacao, safe=False)
