from soluzione_it1.bank import Banca
from soluzione_it1.conto import Conto
from soluzione_it1.cliente import Cliente


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
print(account.cliente.nome_cliente) 