from django.db import models
from django.core.validators import MinValueValidator


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    categoria = models.CharField(max_length=80)
    preco_venda = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    quantidade_atual = models.PositiveIntegerField(default=0)
    estoque_minimo = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class MovimentacaoEstoque(models.Model):
    TIPOS = [
        ("ENTRADA", "Entrada"),
        ("SAIDA", "Saída"),
    ]

    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,
        related_name="movimentacoes"
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPOS
    )
    quantidade = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    data_movimentacao = models.DateTimeField(
        auto_now_add=True
    )
    observacao = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto.nome} - {self.quantidade}"

    class Meta:
        ordering = ["-data_movimentacao"]
        verbose_name = "Movimentação de estoque"
        verbose_name_plural = "Movimentações de estoque"