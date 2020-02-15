import unittest
from collections import OrderedDict
from contas import Conta
from transacoes import Transacao
from services import GerenciaTransacoes


class TestConta(unittest.TestCase):
    
    def test_posso_adicionar_saldo(self):
        conta = Conta(1, 10)
        transacao_negativa = Transacao(1, 100)
        conta.adicionar_saldo(transacao_negativa)
        self.assertEqual(conta.saldo, 110)

    def test_posso_remover_saldo(self):
        conta = Conta(1, 10)
        transacao_negativa = Transacao(1, -100)
        conta.remover_saldo(transacao_negativa)
        self.assertEqual(conta.saldo, -90)

    def test_posso_aplicar_multa(self):
        conta = Conta(1, -10)
        transacao_negativa = Transacao(1, -10)
        conta.aplica_multa(transacao_negativa)
        self.assertEqual(conta.saldo, -15)
    
    def test_nao_posso_aplicar_multa_em_transacoes_de_deposito(self):
        conta = Conta(1, -10)
        transacao_positiva = Transacao(1, 10)
        conta.aplica_multa(transacao_positiva)
        self.assertEqual(conta.saldo, -10)


class TestTransacao(unittest.TestCase):
    
    def test_posso_verificar_se_transacao_e_deposito(self):
        transacao = Transacao(1, 10)
        self.assertFalse(transacao.e_debito)

    def test_posso_verificar_se_transacao_e_debito(self):
        transacao = Transacao(1, -10)
        self.assertTrue(transacao.e_debito)

    def test_posso_recuperar_valor_absoluto_da_transacao(self):
        transacao = Transacao(1, -10)
        self.assertEqual(transacao.valor, 10)


class TestGerenciaTrasacoes(unittest.TestCase):
    
    def test_posso_carregar_dados_das_contas(self):
        contas = OrderedDict()
        contas[1] = 50
        gerencia_transacoes = GerenciaTransacoes()
        gerencia_transacoes.carregar_contas(contas)
        
        for conta in gerencia_transacoes.contas:
            self.assertIsInstance(conta, Conta)

    def test_posso_carregar_dados_das_transacoes(self):
        transacoes = OrderedDict()
        transacoes[1] = 50
        gerencia_transacoes = GerenciaTransacoes()
        gerencia_transacoes.carregar_transacoes(transacoes)
        
        for transacao in gerencia_transacoes.transacoes:
            self.assertIsInstance(transacao, Transacao)

    def test_posso_executar_as_transacoes(self):
        transacao = Transacao(1, 10)
        conta = Conta(1, 10)
        gerencia_transacoes = GerenciaTransacoes()
        gerencia_transacoes.executa_transacao_na_conta(transacao, conta)
        self.assertEqual(conta.saldo, 20)


if __name__ == '__main__':
    unittest.main()