''' Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che produce e vende vari
tipi di prodotti. Gli studenti dovranno creare una classe base chiamata Prodotto e diverse classi
derivate che rappresentano diversi tipi di prodotti. Inoltre, dovranno creare una classe Fabbrica che
gestisce l'inventario e le vendite dei prodotti.


1.Classe Prodotto:

Attributi:
nome (stringa che descrive il nome del prodotto)
costo_produzione (costo per produrre il prodotto)
prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)

Metodi:
calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.


2.Classi Derivate:
Creare almeno due classi derivate da Prodotto, per esempio Elettronica e Abbigliamento.
Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e
garanzia per Elettronica.


3.Classe Fabbrica:

Attributi:
inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.

Metodi:
aggiungi_prodotto: aggiunge prodotti all'inventario.
vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto
realizzato dalla vendita.
resi_prodotto: aumenta la quantità di un prodotto restituito in inventario. '''

class Elettrodomestici:

    def __init__(self, tipo, funzionalità, efficienza_energetica, costo_produzione, prezzo_vendita):
        self.tipo=tipo
        self.funzionalità=funzionalità
        self.efficienza_energetica=efficienza_energetica
        self.costo_produzione=costo_produzione
        self.prezzo_vendita=prezzo_vendita
        self.garanzia=0
    
    def inserisci_garanzia(self, anni_garanzia):
        self.garanzia=anni_garanzia
        return
    
    def sconto(self, percentuale_sconto):
        self.prezzo_vendita=self.prezzo_vendita-((percentuale_sconto/100)*self.prezzo_vendita)
        return
    
    def visualizza_info(self):
        print("Tipo:",self.tipo,"Funzionalità:",self.funzionalità,"Efficienza energetica:",self.efficienza_energetica,"Anni di garanzia:",self.garanzia,"Costo:",self.costo)

    def elenco_prodotti(self):
        dizionario={}

class Fabbrica:

    def __init__(self):
        self.inventario={"Elettrodomestici":[],"Automobili":[]}
    
    def aggiungi_prodotto(self):
        categoria=int(input("Prodotto da aggiungere: 1-Elettrodomestico 2-Automobilistico"))
        if categoria==1: 
            tipo=input("Tipo: ")
            funzionalità=input("Funzionalità: ")
            efficienza_energetica=input("Efficienza energetica: ")
            costo_produzione=float(input("Costo produzione: "))
            prezzo_vendita=float(input("Prezzo vendita: "))
            elettrodomestico = Elettrodomestici(tipo, funzionalità, efficienza_energetica, costo_produzione,prezzo_vendita)    
            n=int(input("Numero",elettrodomestico.tipo,"da aggiungere: "))
            self.inventario["Elettrodomestici"].setdefault(elettrodomestico,0)
            self.inventario["Elettrodomestici"][elettrodomestico]+=n


        # elif categoria==2:
        #     prodotto = Automobili.marca
        #     n=int(input("Numero prodotti da aggiungere: "))
        #     self.inventario["Automobili"].setdefault(prodotto,0)
        #     self.inventario["Automobili"][prodotto]+=n
        else:
            print("Errore")

    def aggiungi_prodotto(self):
        categoria=int(input("Prodotto da vendere: 1-Elettrodomestico 2-Automobilistico"))
        if categoria==1: 
            prodotto=int(input("Elettrodomestico da vendere: "))
            n=int(input("Numero",prodotto,"da vendere: "))
            self.inventario["Elettrodomestici"][prodotto]-=n

        else:
            print("Errore")