from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.cluster.filters import ClusterFilter as ModelFilter
from apps.cluster.forms import ClusterForm as ModelForm
from apps.cluster.models import Cluster as Model
from apps.utils import (
    create_filtered_context,
    paginate_query,
)

APP_NAME = "cluster"
APP_TITLE = "Cluster"


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


class Edit(SuccessMessageMixin, UpdateView):
    model = Model
    form_class = ModelForm
    template_name = f"{APP_NAME}/edit.html"
    success_message = f"{APP_TITLE} Cadastrado"
    extra_context = {"title": APP_TITLE, "app_name": APP_NAME}
    success_url = reverse_lazy(f"{APP_NAME}:index")


def delete(request, pk):
    entry = get_object_or_404(Model, pk=pk)

    if request.method == "POST":
        try:
            entry.delete()
            messages.warning(request, f"{APP_TITLE} Excluído")
        except ProtectedError:
            messages.error(request, f"{APP_TITLE} '{entry.nome}' Não pode ser excluído")
        finally:
            return redirect(f"{APP_NAME}:index")
