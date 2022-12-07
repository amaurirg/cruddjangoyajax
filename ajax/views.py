from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from .form import ProdutoForm
from .models import Categoria, Produto


class CrudView(TemplateView):
    template_name = 'prueba.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context


class CreateCrudCategoria(View):
    def get(self, request):
        nombre1 = request.GET.get('nombre', None)

        obj = Categoria.objects.create(nombre=nombre1)

        categoria = {'id': obj.id, 'nombre': obj.nombre}

        data = {'categoria': categoria}
        return JsonResponse(data)


class DeleteCrudCategoria(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Categoria.objects.get(id=id1).delete()
        data = {'deleted': True}
        return JsonResponse(data)


class UpdateCrudCategoria(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        nombre1 = request.GET.get('nombre', None)

        obj = Categoria.objects.get(id=id1)
        obj.nombre = nombre1
        obj.save()

        categoria = {'id': obj.id, 'nombre': obj.nombre}

        data = {'categoria': categoria}
        return JsonResponse(data)


class ListCategories(View):
    ...
    # def get(self, request):
    #     categorias = Categoria.objects.all()
    #     data = {'categorias': categorias}
    #     # is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    #     # if is_ajax:
    #         # return JsonResponse(data)
    #     return data
    #     # return HttpResponse('dados inválidos')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categorias'] = Categoria.objects.all()
    #     return context


def cria_produto(request):
    # text = request.GET.get('button_text')
    # is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    # if is_ajax:
    #     return JsonResponse({'seconds': time()})
    # return render(request, 'app/index.html')
    text = request.GET.get('nome')
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        obj = Categoria.objects.create(nombre=text)
        data = {'id': obj.id, 'nova_categoria': obj.nombre}
        return JsonResponse(data)
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect(reverse('crud_ajax'))
        # return redirect(reverse('modal_cria_candidato'))
    return render(request, 'cria_produto.html', {'form': form})


class Cria_Categoria(View):
    # text = request.GET.get('button_text')
    # is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    # if is_ajax:
    #     return JsonResponse({'seconds': time()})
    # return render(request, 'app/index.html')
    def get(self, request):
        text = request.GET.get('nome')
        # is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        # if is_ajax:
        obj = Categoria.objects.create(nombre=text)
        categoria = {'id': obj.id, 'nombre': obj.nombre}
        data = {'categoria': categoria}
        return JsonResponse(data)
        # form = ProdutoForm(request.POST or None)
        # if form.is_valid():
        #     form.save()
        # return render(request, 'cria_produto.html', {'form': form})


def produtos(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            produtos = list(Produto.objects.all().values())
            return JsonResponse({'produtos': produtos})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')