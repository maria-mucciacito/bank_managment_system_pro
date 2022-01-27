class Banca:
    
    def __init__(self,nome_banca):
        self.nome_banca = nome_banca
        self.clienti = []
        self.conti_correnti = []

    def __repr__(self):
        return f"Nome Banca: {self.nome_banca}, numero totale di clienti: {self.clienti}, numero totale di conti correnti: {self.conti_correnti}"