from django import forms
from .models import Produto, MovimentacaoEstoque


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "nome",
            "categoria",
            "preco_venda",
            "quantidade_atual",
            "estoque_minimo",
        ]
        labels = {
            "nome": "Nome do produto",
            "categoria": "Categoria",
            "preco_venda": "Preço de venda (R$)",
            "quantidade_atual": "Quantidade inicial",
            "estoque_minimo": "Estoque mínimo",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "categoria": forms.TextInput(attrs={"class": "form-control"}),
            "preco_venda": forms.NumberInput(
                attrs={"class": "form-control", "min": "0", "step": "0.01"}
            ),
            "quantidade_atual": forms.NumberInput(
                attrs={"class": "form-control", "min": "0"}
            ),
            "estoque_minimo": forms.NumberInput(
                attrs={"class": "form-control", "min": "0"}
            ),
        }

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ["produto", "tipo", "quantidade", "observacao"]

        labels = {
            "produto": "Produto",
            "tipo": "Tipo de movimentação",
            "quantidade": "Quantidade",
            "observacao": "Observação (opcional)",
        }

        widgets = {
            "produto": forms.Select(attrs={"class": "form-select"}),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "quantidade": forms.NumberInput(
                attrs={"class": "form-control", "min": "1", "step": "1"}
            ),
            "observacao": forms.TextInput(
                attrs={"class": "form-control"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["produto"].queryset = Produto.objects.filter(
            ativo=True
        )        