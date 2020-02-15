import csv
import argparse
from contas import Conta
from transacoes import Transacao
from services import GerenciaTransacoes

parser = argparse.ArgumentParser()
parser.add_argument('contas_csv')
parser.add_argument('transacoes_csv')
args = parser.parse_args()

def main():
    gerencia_transacoes = GerenciaTransacoes()
    gerencia_transacoes.carregar_dados(args.contas_csv, args.transacoes_csv)
    gerencia_transacoes.execute()
    gerencia_transacoes.exibir_saldos()
    
    return 

if __name__ == "__main__":
    main()