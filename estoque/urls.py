from django.urls import path
from . import views

urlpatterns = [
    path(
        "produtos/novo/",
        views.cadastrar_produto,
        name="cadastrar_produto",
    ),
    path(
        "estoque/",
        views.consultar_estoque,
        name="consultar_estoque",
    ),
]