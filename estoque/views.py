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