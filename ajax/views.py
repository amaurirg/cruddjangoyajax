from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import  Categoria

class CrudView(TemplateView):
    template_name = 'prueba.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class CreateCrudCategoria(View):
    def get(self, request):
        nombre1 = request.GET.get('nombre', None)

        obj = Categoria.objects.create(
            nombre=nombre1,

        )

        categoria = {'id': obj.id, 'nombre': obj.nombre}

        data = {
            'categoria': categoria
        }
        return JsonResponse(data)


class DeleteCrudCategoria(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Categoria.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudCategoria(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        nombre1 = request.GET.get('nombre', None)

        obj = Categoria.objects.get(id=id1)
        obj.nombre = nombre1
        obj.save()

        categoria = {'id': obj.id, 'nombre': obj.nombre}

        data = {
            'categoria': categoria
        }
        return JsonResponse(data)

