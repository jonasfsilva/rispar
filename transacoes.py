class Transacao:
    
    identificador_conta = 0
    _valor_original = 0
    
    def __init__(self, identificador_conta, valor):
        self.identificador_conta = identificador_conta
        self._valor_original = int(valor)
    
    def __repr__(self):
        return "{0},{1}".format(
            self.identificador_conta, self.valor)
    
    @property
    def valor(self):
        return abs(self._valor_original)

    @property
    def e_debito(self):
        if self._valor_original < 0:
            return True
        return False
