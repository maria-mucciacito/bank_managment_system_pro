from logging import exception


class Conto:
    tassa_prelievo = 1.00

    def __init__(self, numero_conto, cliente, saldo=0):
        self.__numero_conto = numero_conto
        self.__cliente = cliente
        self.__saldo = saldo 
        self.__id = id(self)
        print(f'Istanza banca creata con id: {self.__id}')

    # Definizione di getter e setter #
    @property
    def id(self): 
        return self.__id
        
    @property
    def numero_conto(self): 
        return self.__numero_conto
    
    @numero_conto.setter
    def numero_conto(self, numero_conto): 
        self.__numero_conto = numero_conto

    @property
    def cliente(self): 
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente): 
        self.__cliente = cliente

    @property
    def saldo(self): 
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo): 
        self.__saldo = saldo

    def versa_soldi(self, value): 
        self.__saldo += value
    
    def preleva_soldi(self, value): 
        value += self.tassa_prelievo
        if self.__saldo < value: 
            print('Importo richiesto non presente sul conto')
        else: 
            self.__saldo -= value
            print(f'Hai prelevato é {value}. Nuovo saldo del conto: {self.__saldo}')

    def __repr__(self):
        return "Conto " + self.numero_conto + " intestato a cliente " + self.cliente.nome_cliente  + " con saldo " + str(self.saldo) + "€"
        
import datetime


class Contospecial(Conto):
    tassa_prelievo = 2.00
    data_inizio_debito = None

    
    def preleva_soldi(self, value): 
        value += self.tassa_prelievo
        self.__saldo -= value
        if (self.saldo < 0):
            if (self.data_inizio_debito == None):
                self.data_inizio_debito = datetime.datetime.now()
        print(f'Hai prelevato é {value}. Nuovo saldo del conto: {self.__saldo}')

    def versa_soldi(self, value):
        return super().versa_soldi(value)
        if (self.saldo >= 0):
            self.data_inizio_debito = None
            print('Il saldo è tornato positivo')