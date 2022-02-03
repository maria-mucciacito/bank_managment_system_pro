


class Cliente:

    def __init__(self,nome_cliente,numero_telefono):
        self.__id = id(self)
        self.__nome_cliente = nome_cliente
        self.__numero_telefono = numero_telefono

    def __repr__(self):
        return f"Id {self.id} Cliente {self.nome_cliente} telefono {self.numero_telefono}"

    def __get_id(self):
        return self.__id
    id = property(__get_id,)

    def __get_nome_cliente(self):
        return self.__nome_cliente
    def __set_nome_cliente(self,nome_cliente):
        self.__nome_cliente = nome_cliente
    
    nome_cliente = property(__get_nome_cliente,__set_nome_cliente)

    def __get_numero_telefono(self):
        return self.__numero_telefono
    def __set_numero_telefono(self,numero_telefono):
        self.__numero_telefono = numero_telefono
    
    numero_telefono = property(__get_numero_telefono,__set_numero_telefono)

