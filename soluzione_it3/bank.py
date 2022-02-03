from soluzione_it3.utility import Utility


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

    def __get_clienti(self):
        return self.__clienti
    clienti = property(__get_clienti)
    def __get_conti_correnti(self):
        return self.__conti_correnti
    conti_correnti = property(__get_conti_correnti)

    def apri_conto_corrente(self,conto):
        self.__conti_correnti.append(conto)

    def aggiungi_cliente(self,cliente):
        self.__clienti.append(cliente)

    def chiudi_conto_corrente(self, numero_conto): 
        assert Utility.is_integer(numero_conto), "Inserire un numero intero"        
        assert int(numero_conto) > 0, "Inserire un numero valido"
        
        pos=-1
        for index in range(0, len(self.conti_correnti)): 
            if self.conti_correnti[index].numero_conto == int(numero_conto):
                pos = index
                break
            
        if pos<0: 
            print("ERROR: numero conto non trovato")
        else: 
            self.conti_correnti.pop(pos)
            print("conto corrente numero " + str(numero_conto) + " rimosso con successo")
    
    def rimuovi_cliente(self, id): 
        assert Utility.is_integer(id), "Inserire un id intero"        
        assert int(id) > 0, "Inserire un id valido"
        
        pos=-1
        for index in range(0, len(self.clienti)): 
            if self.clienti[index].id == int(id):
                pos = index
                break
            
        if pos<0: 
            print("ERROR: id cliente non trovato")
        else: 
            self.clienti.pop(pos)
            print("cliente " + str(id) + " rimosso con successo")
    
    
