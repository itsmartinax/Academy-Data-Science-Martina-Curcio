# ESERCIZIO CLASSE
'''Crea una classe biblioteca che permetta di creare un libro e stamparlo.
Extra: permetti di creare quanti libri vuole l’utente.'''

from EsercizioC2 import Libro

class Biblioteca():

    def __init__(self):
        self.libri = []

    def aggiungi_libro(self):
        titolo=input("Inserisci titolo: ")
        autore=input("Inserisci autore: ")
        pagine=int(input("Inserisci numero pagine: "))
        libro = Libro(titolo, autore, pagine)
        self.libri.append(libro)
    
    def trova_libro(self, titolo=" ", autore=" ", pagine=0):
        # titolo=input("Inserisci titolo o premi invio per saltare: ")
        # autore=input("Inserisci autore o premi invio per saltare: ")
        # pagine=input("Inserisci numero pagine o premi invio per saltare: ")
        for libro in self.libri:
            if (titolo == libro.titolo or titolo == " ") and (autore==libro.autore or autore == " ") and (pagine==libro.pagine or pagine == 0):
                print("Libro trovato!\nTitolo:",libro.titolo,"Autore:",libro.autore,"Pagine:",libro.pagine)
            else:
                print("Libro non trovato!\nVuoi inserire un nuovo libro? (s/n)")
                Biblioteca.aggiungi_libro(self)





#ESEMPIO
Biblioteca1 = Biblioteca()
Biblioteca1.aggiungi_libro()
Biblioteca1.aggiungi_libro()
Biblioteca1.trova_libro(autore="martina")
Biblioteca1.trova_libro(titolo="ciao", autore="lollo")
