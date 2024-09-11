class Automobile: # dichiaro la classe

    numero_di_ruote = 4 # attributo di classe

    def __init__(self, marca, modello): # metodo costruttore
        self.marca = marca # attributo di istanza
        self.modello = modello # attributo di istanza

    def stampa_info(self): # metodo di istanza (richiama l'oggetto)
        print("L'automobile è una", self.marca, self.modello)


Auto1 = Automobile("Fiat","500") #il self diventa Auto1
Auto2 = Automobile("BMW","X3") #il self diventa Auto2

Auto1.stampa_info()

