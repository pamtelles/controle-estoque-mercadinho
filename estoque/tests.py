
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import MovimentacaoEstoque, Produto


class EstoqueTests(TestCase):

    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="usuario_teste",
            password="SenhaSegura123!"
        )
        self.client.force_login(self.usuario)

        self.produto = Produto.objects.create(
            nome="Arroz Branco 5 kg",
            categoria="Alimentos",
            preco_venda=Decimal("25.90"),
            quantidade_atual=20,
            estoque_minimo=5,
            ativo=True
        )

    def test_cadastrar_produto(self):
        resposta = self.client.post(
            reverse("cadastrar_produto"),
            {
                "nome": "Feijão Carioca 1 kg",
                "categoria": "Alimentos",
                "preco_venda": "8.90",
                "quantidade_atual": 4,
                "estoque_minimo": 5,
            }
        )

        self.assertEqual(resposta.status_code, 302)
        self.assertTrue(
            Produto.objects.filter(
                nome="Feijão Carioca 1 kg"
            ).exists()
        )

    def test_entrada_aumenta_estoque(self):
        resposta = self.client.post(
            reverse("registrar_movimentacao"),
            {
                "produto": self.produto.pk,
                "tipo": "ENTRADA",
                "quantidade": 10,
                "observacao": "Recebimento de mercadoria",
            }
        )

        self.produto.refresh_from_db()

        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(self.produto.quantidade_atual, 30)
        self.assertEqual(MovimentacaoEstoque.objects.count(), 1)

    def test_saida_diminui_estoque(self):
        resposta = self.client.post(
            reverse("registrar_movimentacao"),
            {
                "produto": self.produto.pk,
                "tipo": "SAIDA",
                "quantidade": 3,
                "observacao": "Venda de mercadoria",
            }
        )

        self.produto.refresh_from_db()

        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(self.produto.quantidade_atual, 17)
        self.assertEqual(MovimentacaoEstoque.objects.count(), 1)

    def test_saida_maior_que_saldo_e_bloqueada(self):
        resposta = self.client.post(
            reverse("registrar_movimentacao"),
            {
                "produto": self.produto.pk,
                "tipo": "SAIDA",
                "quantidade": 50,
                "observacao": "Tentativa de retirada",
            }
        )

        self.produto.refresh_from_db()

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(self.produto.quantidade_atual, 20)
        self.assertEqual(MovimentacaoEstoque.objects.count(), 0)
        self.assertContains(
            resposta,
            "Quantidade insuficiente em estoque."
        )

    def test_consulta_exibe_produto(self):
        resposta = self.client.get(
            reverse("consultar_estoque")
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Arroz Branco 5 kg")

    def test_usuario_nao_autenticado_e_redirecionado(self):
        self.client.logout()

        resposta = self.client.get(
            reverse("consultar_estoque")
        )

        self.assertEqual(resposta.status_code, 302)
        self.assertIn("/admin/login/", resposta.url)
