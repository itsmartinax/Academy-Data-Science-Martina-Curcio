''' Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
1.Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e
tipo_cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere
impostato su False di default (cioè, il ristorante è chiuso).
Un dizionario menu dove dentro ci sono i piatti e prezzi che ha il ristorante
2.Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il
tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che
il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica
che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu
3.Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto. '''

class Ristorante:

    def __init__(self,nome,tipo_cucina):
        self.nome=nome
        self.tipo_cucina=tipo_cucina
        self.aperto = False
        self.menu = {}

    def descrivi_ristorante(self):
        print("Il ristorante",self.nome,"è uno dei migliori ristoranti di cucina",self.tipo_cucina)

    def stato_apertura(self):
        if self.aperto==False:
            print("Il ristorante è chiuso")
        else:
            print("Il ristorante è aperto")
    
    def apri_ristorante(self):
        self.aperto=True
        print("Il ristorante ora è aperto!")
    
    def chiudi_ristorante(self):
        self.aperto=False
        print("Il ristorante ora è chiuso!")

    def aggiungi_al_menu(self):
        piatto=input("Piatto da aggiungere: ")
        prezzo=float(input("Prezzo del piatto "+piatto+": "))
        self.menu[piatto]=prezzo

    def togli_dal_menu(self):
        piatto=input("Piatto da togliere: ")
        if piatto in self.menu:
            del self.menu[piatto]
        else:
            print("Il piatto non è nel menù!")
    
    def stampa_menu(self):
        for piatto in self.menu:
            print(piatto, self.menu[piatto])



Rist1=Ristorante("Da Martina", "italiana")
Rist1.descrivi_ristorante()

Rist1.stato_apertura()
Rist1.apri_ristorante()
Rist1.stato_apertura()
Rist1.chiudi_ristorante()
Rist1.stato_apertura()

# Rist1.aggiungi_al_menu()
# Rist1.aggiungi_al_menu()
# Rist1.stampa_menu()
# Rist1.togli_dal_menu()
# Rist1.stampa_menu()


    

    