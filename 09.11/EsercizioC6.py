class Prodotto:

    def __init__(self,tipo,costo_produzione,prezzo_vendita):
        self.tipo=tipo
        self.costo_produzione=costo_produzione
        self.prezzo_vendita=prezzo_vendita
    
    def profitto(self):
        diff=self.prezzo_vendita-self.costo_produzione
        return diff
    
    def sconto(self, percentuale_sconto):
        self.prezzo_vendita=self.prezzo_vendita-((percentuale_sconto/100)*self.prezzo_vendita)
        return
    
    def mostra_informazioni(self):
        print(self.tipo,"ha un costo di produzione",self.costo_produzione,"e prezzo di vendita",self.prezzo_vendita)


class Elettrodomestici(Prodotto):

    def __init__(self, tipo, costo_produzione, prezzo_vendita, efficienza_energetica):
        Prodotto.__init__(self,tipo,costo_produzione,prezzo_vendita)
        self.efficienza_energetica=efficienza_energetica
        self.garanzia=0
    
    def inserisci_garanzia(self, anni_garanzia):
        self.garanzia=anni_garanzia
        return
    
    def mostra_informazioni(self):
        super().mostra_informazioni()
        print(self.tipo,"ha efficienza energetica",self.efficienza_energetica,"e",self.garanzia,"anni di garanzia.")


class Veicoli(Prodotto):

    def __init__(self, tipo, costo_produzione, prezzo_vendita, motore, nruote):
        Prodotto.__init__(self,tipo,costo_produzione,prezzo_vendita)
        self.motore=motore
        self.nruote=nruote

    def mostra_informazioni(self):
        super().mostra_informazioni()
        print(self.tipo,"ha un motore a",self.motore,"e",self.garanzia,"ruote.")



