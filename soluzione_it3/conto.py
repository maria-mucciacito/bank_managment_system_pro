
from soluzione_it2 import cliente

class Conto:

    def __init__(self,numero_conto, cliente,bilancio_conto=0, saldo=0):
        self.__bilancio_conto = bilancio_conto
        self.__numero_conto = numero_conto
        self.__saldo = saldo    
        self.__cliente = cliente
        self.__operazioni_effettuate = []

    def __repr__(self):
        return f"Conto {self.numero_conto}, intestato a cliente {self.cliente.nome_cliente}, con saldo {self.saldo} €"

    def __get_bilancio_conto(self):
        return self.__bilancio_conto
    def __set_bilancio_conto(self,bilancio_conto):
        self.__bilancio_conto = bilancio_conto
    bilancio_conto = property(__get_bilancio_conto,__set_bilancio_conto)

    def __get_numero_conto(self):
        return self.__numero_conto
    def __set_numero_conto(self,numero_conto):
        self.__numero_conto = numero_conto
    numero_conto = property(__get_numero_conto,__set_numero_conto)

    def __get_saldo(self):
        return self.__saldo
    def __set_saldo(self,saldo):
        self.__saldo = saldo
    saldo = property(__get_saldo,__set_saldo)

    def __get_cliente(self):
        return self.__cliente
    def __set_cliente(self,cliente):
        self.__cliente = cliente
    cliente = property(__get_cliente,__set_cliente)

    def versa_soldi(self,value):
        self.__saldo = self.__saldo + value
        print('operazione effettuata')

    def preleva_soldi(self,value):
        if (value > self.__saldo):
            raise 'impossibile prelevare'
        else:
            self.__saldo = self.__saldo - value


