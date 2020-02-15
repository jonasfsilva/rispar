class Conta:

    identificador = 0
    saldo = 0
    multa = 5
    
    def __init__(self, identificador, saldo):
        self.identificador = identificador
        self.saldo = int(saldo)

    def __str__(self):
        return "{0},{1}".format(
            self.identificador, self.saldo)    

    def adicionar_saldo(self, transacao):
        self.saldo += transacao.valor

    def remover_saldo(self, transacao):
        self.saldo -= transacao.valor

    def executa_transacao(self, transacao):
        if transacao.e_debito:
            self.remover_saldo(transacao)
        else:
            self.adicionar_saldo(transacao)
            
        self.aplica_multa(transacao)

    def aplica_multa(self, transacao):
        if self.saldo < 0 and transacao.e_debito:
            self.saldo -= self.multa 
