
class Conto:

    def __init__(self,numero_conto, cliente,bilancio_conto=0, saldo=0):
        self.bilancio_conto = bilancio_conto
        self.numero_conto = numero_conto
        self.saldo = saldo    
        self.cliente = cliente
        self.operazioni_effettuate = []

    def __repr__(self):
        return f"Conto {self.numero_conto}, intestato a cliente {self.cliente.nome_cliente}, con saldo {self.saldo} €"


