'''from soluzione_it2.bank import Banca
from soluzione_it2.conto import Conto
from soluzione_it2.cliente import Cliente


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
print(account.cliente.nome_cliente)'''

from soluzione_it3.cliente import Cliente
from soluzione_it3.bank import Banca
from soluzione_it3.conto import Conto

# CODICE DI TEST. Rispondi alle domande scritte nei commenti #
cliente1 = Cliente(0, 'Davide', '3924663077')
cliente2 = Cliente(1, 'Simona', '3335688985')
cliente3 = Cliente(2, 'Marco', '3335688285')
banca_san_paolo = Banca('Banca San Paolo')

conto1 = Conto(1587,cliente1)
conto2 = Conto(1588,cliente1)
conto3 = Conto(1685,cliente2)
conto4 = Conto(1987,cliente3)

banca_san_paolo.aggiungi_cliente(cliente1)
banca_san_paolo.aggiungi_cliente(cliente2)
banca_san_paolo.aggiungi_cliente(cliente3)
banca_san_paolo.apri_conto_corrente(conto1)
banca_san_paolo.apri_conto_corrente(conto2)
banca_san_paolo.apri_conto_corrente(conto3)
banca_san_paolo.apri_conto_corrente(conto4)

# RISPONDI ALLE DOMANDE SCRITTE NEI COMMENTI * 

#1. OUTPUT PREVISTO:  
print(banca_san_paolo)


#2. OUTPUT PREVISTO
print(cliente1)
print(cliente2)
print(cliente3)


#3. OUTPUT PREVISTO
#banca_san_paolo.rimuovi_cliente(155)
#print(banca_san_paolo)


#4. OUTPUT PREVISTO
banca_san_paolo.rimuovi_cliente(2)
print(banca_san_paolo)


#5. OUTPUT PREVISTO
banca_san_paolo.aggiungi_cliente(50)
print(banca_san_paolo)


#6. OUTPUT PREVISTO
#conto4 = Conto(1990,cliente3)
#banca_san_paolo.aggiungi_conto_corrente(conto4)
#print(banca_san_paolo)
