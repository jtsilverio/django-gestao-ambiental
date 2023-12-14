from django.core import serializers
from django.http import JsonResponse

from apps.cidades.models import Cidades as Model


def get_cidades(request):
    estado = request.GET.get("estado")
    cidades = Model.objects.filter(estado=estado)
    cidades = serializers.serialize("json", cidades)
    return JsonResponse(cidades, safe=False)
