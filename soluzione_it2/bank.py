class Banca:
    
    def __init__(self,nome_banca):
        self.__nome_banca = nome_banca
        self.__clienti = []
        self.__conti_correnti = []

    def __repr__(self):
        return f"Nome Banca: {self.nome_banca}, numero totale di clienti: {self.__clienti}, numero totale di conti correnti: {self.__conti_correnti}"

    def __get_nome_banca(self):
        return self.__nome_banca
    def __set_nome_banca(self,nome_banca):
        self.__nome_banca = nome_banca
    nome_banca = property(__get_nome_banca,__set_nome_banca)


