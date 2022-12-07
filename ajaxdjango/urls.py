"""ajaxdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ajax.views import (
    CrudView, CreateCrudCategoria, DeleteCrudCategoria,
    UpdateCrudCategoria, ListCategories, cria_produto, Cria_Categoria, produtos,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Django Ajax CRUD Operations
    path('', CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', CreateCrudCategoria.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', DeleteCrudCategoria.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', UpdateCrudCategoria.as_view(), name='crud_ajax_update'),
    path('ajax/crud/categorias/', ListCategories.as_view(), name='crud_ajax_list'),
    path('cria_produto/', cria_produto, name='crud_ajax_list'),
    # path('cria_produto/', Cria_Categoria.as_view(), name='cria_categoria'),
    path('produtos/', produtos, name='produtos'),
]
