import csv
from collections import OrderedDict
from transacoes import Transacao 
from contas import Conta 


class GerenciaTransacoes:

    contas = []
    transacoes = []

    def ler_csv(self, filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            linhas = OrderedDict() 
            for row in csv_reader:
                linhas[row[0]] = row[1]
        return linhas
    
    def valida_registros(self, registros):
        for identificador, valor in registros.items():
            try:
                int(identificador)
                int(valor)
            except ValueError:
                raise ValueError("Valor invalid: id: {0} | valor {1}".format(
                    identificador, valor))

    def carregar_dados(self, contas_csv, transacoes_csv):
        contas_linhas = self.ler_csv(contas_csv)
        transacoes_linhas = self.ler_csv(transacoes_csv)
        self.carregar_contas(contas_linhas)
        self.carregar_transacoes(transacoes_linhas)
    
    def carregar_contas(self, contas_linhas):
        self.valida_registros(contas_linhas)
        for conta_id, conta_saldo  in contas_linhas.items():
            self.contas.append(Conta(conta_id, conta_saldo))

    def carregar_transacoes(self, transacoes_linhas):
        self.valida_registros(transacoes_linhas)
        for transacao_id, transacao_valor in transacoes_linhas.items():
            self.transacoes.append(Transacao(transacao_id, transacao_valor))

    def executa_transacao_na_conta(self, transacao, conta):
        if conta.identificador == transacao.identificador_conta:
            conta.executa_transacao(transacao)

    def exibir_saldos(self):
        [print(conta) for conta in self.contas]

    def execute(self):
        for transacao in self.transacoes:
            for conta in self.contas:
                self.executa_transacao_na_conta(transacao, conta)
