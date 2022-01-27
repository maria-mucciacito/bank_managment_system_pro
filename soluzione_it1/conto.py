from cliente import Cliente
from bank import Banca


class Conto:

    def __init__(self,numero_conto, cliente,bilancio_conto=0, saldo=0):
        self.bilancio_conto = bilancio_conto
        self.numero_conto = numero_conto
        self.saldo = saldo    
        self.cliente = cliente
        self.operazioni_effettuate = []

    def __repr__(self):
        return f"Conto {self.numero_conto}, intestato a cliente {self.cliente.nome_cliente}, con saldo {self.saldo}"



'''
 #CODICE DI TEST. Rispondi alle domande scritte nei commenti 
cliente1 = Cliente('Davide', '3924663077')
cliente2 = Cliente('Simona', '3335688985')
cliente3 = Cliente('Marco', '3335688285')
banca_san_paolo = Banca('Banca San Paolo')
account = Conto('00001',cliente1)

print(account)
print(banca_san_paolo)
print(cliente1)

print( cliente1.nome_cliente )
print(account.cliente.nome_cliente) '''