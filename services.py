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
            lines = OrderedDict() 
            for row in csv_reader:
                lines[row[0]] = row[1]
        return lines

    def carregar_dados(self, contas_csv, transacoes_csv):
        transacoes_lines = self.ler_csv(transacoes_csv)
        contas_lines = self.ler_csv(contas_csv)
        self.carregar_contas(contas_lines)
        self.carregar_transacoes(transacoes_lines)
    
    def carregar_contas(self, contas_lines):
        for conta_id, conta_saldo  in contas_lines.items():
            self.contas.append(Conta(conta_id, conta_saldo))

    def carregar_transacoes(self, transacoes_lines):
        for transacao_id, transacao_valor in transacoes_lines.items():
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
