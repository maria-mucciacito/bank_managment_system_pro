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

    def apri_conto_corrente(self,conto):
        self.__conti_correnti.append(conto)

    def aggiungi_cliente(self,cliente):
        self.__clienti.append(cliente)

    def chiudi_conto_corrente(self,numero_conto):
        if numero_conto in self.__conti_correnti:
            self.__conti_correnti.remove(numero_conto)
        else:
            raise 'elemento non presente nella lista'

    def rimuovi_cliente(self,id):
        if id in self.__clienti:
            self.__clienti.remove(id)
            print('elemento eliminato')
        else:
            raise 'elemento non presente nella lista' 

    
