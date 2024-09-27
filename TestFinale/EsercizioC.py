# ESERCIZIO CLASSI
''' Crea una classe chiamata Libro. Questa classe dovrebbe avere:
Tre attributi: titolo, autore e pagine.
Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto
da 'autore' e ha 'pagine' pagine." '''

class Libro:

    def __init__(self,titolo,autore,pagine):
        self.titolo=titolo
        self.autore=autore
        self.pagine=pagine
    
    #def descrizione(self,):
    #    print("Il libro",self.titolo,"è stato scritto da",self.autore,"e ha",self.pagine,"pagine.")
