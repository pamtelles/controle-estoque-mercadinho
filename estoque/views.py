from django.db import transaction
from django.db.models import F
from django.db.models.functions import Greatest
from .forms import MovimentacaoForm
from .models import Produto
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProdutoForm


@login_required
def cadastrar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect("cadastrar_produto")
    else:
        form = ProdutoForm()

    return render(
        request,
        "estoque/cadastrar_produto.html",
        {"form": form},
    )

@login_required
def consultar_estoque(request):
    busca = request.GET.get("busca", "").strip()

    produtos = Produto.objects.filter(ativo=True)

    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    return render(
        request,
        "estoque/consultar_estoque.html",
        {
            "produtos": produtos,
            "busca": busca,
        },
    )

@login_required
def registrar_movimentacao(request):
    if request.method == "POST":
        form = MovimentacaoForm(request.POST)

        if form.is_valid():
            movimentacao = form.save(commit=False)

            with transaction.atomic():
                produto = Produto.objects.select_for_update().get(
                    pk=movimentacao.produto_id,
                    ativo=True
                )

                if movimentacao.tipo == "SAIDA":
                    if produto.quantidade_atual < movimentacao.quantidade:
                        form.add_error(
                            "quantidade",
                            "Quantidade insuficiente em estoque."
                        )
                    else:
                        produto.quantidade_atual -= movimentacao.quantidade

                elif movimentacao.tipo == "ENTRADA":
                    produto.quantidade_atual += movimentacao.quantidade

                if not form.errors:
                    produto.save(update_fields=["quantidade_atual"])
                    movimentacao.save()

                    messages.success(
                        request,
                        "Movimentação registrada com sucesso!"
                    )
                    return redirect("consultar_estoque")
    else:
        form = MovimentacaoForm()

    return render(
        request,
        "estoque/registrar_movimentacao.html",
        {"form": form},
    )