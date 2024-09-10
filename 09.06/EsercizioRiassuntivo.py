# ESERCIZIO RIASSUNTIVO

## DEFINIZIONE E CARATTERISTICHE DI PYTHON

#DEFINIZIONE PYTHON
def definizione_python():
    print("Python è un linguaggio di programmazione interpretato, orientato agli oggetti, dinamico e ad alto livello.")
    chk=True
    while chk==True:
        opt = int(input("Quale termine vuoi approfondire?\n1-Interpretato \n2-Orientato agli oggetti \n3-Dinamico \n4-Alto livello \n5-Esci \nInserisci opzione: "))
        if opt==1:
            print("Linguaggio interpretato: \n Un interprete analizza il codice sorgente e, se sintatticamente corretto, lo esegue.")
        elif opt==2:
            introduzione_OOP()
        elif opt==3:
            print("Linguaggio dinamico: \n Le variabili non necessitano di essere dichiarare esplicitamente con un tipo prima di essere utilizzate.")
        elif opt==4:
            print("Linguaggio ad alto livello: \n Linguaggio informatico progettato per essere più simile al linguaggio naturale.")
        elif opt==5:
            chk=False
        else:
            print("Errore")
    return

#INTRODUZIONE OOP
def introduzione_OOP():
    print("Linguaggio orientato agli oggetti: \n La programmazione orientata agli oggetti è un paradigma di programmazione che si fonda sul concetto di 'oggetto'. Basata sull'astrazione che è la madre delle tre regole fondamentali dell'OOP: \n-Incapsulamento \n-Ereditarietà \n-Polimorfismo")
    chk=True
    while chk==True:
        opt = int(input("Quale concetto vuoi approfondire?\n1-Astrazione \n2-Incapsulamento \n3-Ereditarietà \n4-Polimorfismo \n5-Esci \nInserisci opzione: "))
        if opt==1:
            print("Astrazione: \nConsiste nel creare una rappresentazione semplificata di un oggetto, focalizzandosi sugli aspetti rilevanti e nascondendo i dettagli meno importanti.")
        elif opt==2:
            print("Incapsulamento: \nGli oggetti nascondono i propri dati e li rendono accessibili solo attraverso metodi specifici.")
        elif opt==3:
            print("Ereditarietà: \nUna classe può ereditare proprietà e comportamenti da un'altra classe in maniera gerarchica.")
        elif opt==4:
            print("Polimorfismo: \nCapacità di un oggetto di cambiare forma ma non comportamento e viceversa.")
        elif opt==5:
            chk=False
        else:
            print("Errore")
    return

#CARATTERISTICHE PYTHON
def caratteristiche_python():
    chk=True
    while chk==True:
        opt = int(input("Quale caratteristica vuoi approfondire?\n1-Tolleranza agli errori \n2-Sintasi leggibile e pulita \n3-Filosofia 'Batteries Included' \n4-Dinamico ma fortemente tipizzato \n5-Supporto multiparadigma \n6-Estensibilità e Interoperabilità \n7-Esci \nInserisci opzione: "))
        if opt==1:
            print("Tolleranza agli errori: \n Permette di correggere errori senza dover ricompilare l'intero programma.")
        elif opt==2:
            print("Sintasi leggibile e pulita: \n La sintassi risulta essere chiara e leggile, vicino al linguaggio naturale.")
        elif opt==3:
            print("Filosofia 'Batteries Included': \n Python fornisce una vasta gamma di librerie standard, utili per compiti comuni in programmazione.")
        elif opt==4:
            print("Dinamico ma fortemente tipizzato: \n Le variabili non necessitano di essere dichiarate esplicitamente con un tipo, tuttavia, è fortemente tipizzato in quanto non sono concesse operazioni che non siano ben definite.")
        elif opt==5:
            print("Supporto multiparadigma: \n Python supporta diversi paradigmi di programmazione permettendo di scegliere l'approccio più adatto per un problema.")
        elif opt==6:
            print("Estensibilità e Interoperabilità: \n Python può essere esteso con codice scritto in altri linguaggi e permette la modifica delle librerie preesistenti.")
        elif opt==7:
            chk=False
        else:
            print("Errore")
    return

#MAIN PYTHON
def python():
    definizione_python()
    caratteristiche_python()
    return



## DEFINIZIONE E CARATTERISTICHE DELL'UML

#CARATTERISTICHE UML
def caratteristiche_UML():
    chk=True
    while chk==True:
        opt = int(input("Quali caratteristiche vuoi conoscere? \n1-Standardizzato \n2-Visuale \n3-Polivalente \n4-Estensibile \n5-Esci \nInserisci opzione: "))
        if opt==1:
            print("Standardizzato: \n Le sue specifiche sono uniformi e riconosciute a livello internazionale.")
        elif opt==2:
            print("Visuale: \n Utilizza diagrammi per rappresentare gli elementi e le relazioni in un sistema software.")
        elif opt==3:
            print("Polivalente: \n Modella sistemi di vario tipo.")
        elif opt==4:
            print("Estensibile: \n Permette la personalizzazione delle regole a patto che le nuove siano coerenti con le precedenti.")
        elif opt==5:
            chk=False
        else:
            print("Errore")
    return


#ELEMENTI FONDAMENTALI
def elementi_UML():
    chk=True
    while chk==True:
        opt = int(input("1-Strutture statiche \n2-Comportamenti dinamici  \n3-Aspetti di organizzazione \n4-Esci \nInserisci opzione: "))
        if opt==1:
            print("Strutture statiche: \n Elementi irremovibili che rappresentano gli obblighi che hanno macchina e utente.")
        elif opt==2:
            print("Comportamenti dinamici: \n Azioni pratiche che variano nel tempo.")
        elif opt==3:
            print("Aspetti di organizzazione: \n Insieme delle regole comuni con cui si visualizza l'UML, anche dette stereotipi.")
        elif opt==3:
            chk=False
        else:
            print("Errore")
    return

#MAIN UML
def UML():
    print("L'UML è un linguaggio standardizzato per la modellizazione di software.")
    chk=True
    while chk==True:
        opt = int(input("Cosa vuoi sapere?\n1-Caratteristiche \n2-Elementi fondamentali \n3-Esci \nInserisci opzione: "))
        if opt==1:
            caratteristiche_UML()
        elif opt==2:
            elementi_UML()
        elif opt==3:
            chk=False
        else:
            print("Errore")
    return



## VARIABILI IN PYTHON
def numeri():
    print("Ci sono principalmente due tipi di numeri: \n1-Interi \n2-Numeri in virgola mobile")
    x=int(input("Inserisci un numero intero: "))
    print(x,"è di tipo",type(x))
    y=float(input("Inserisci un numero con la virgola: "))
    print(y,"è di tipo",type(y))
    return

def stringhe():
    print("Le stringhe sono sequenze di caratteri.")
    s=input("Inserisci una frase: ")
    print(s,"è di tipo",type(s))
    chk=True
    while chk==True:
        opt = int(input("Quale metodo vuoi applicare sulla stringa?\n1-len() \n2-upper() \n3-lower() \n4-split() \n5-replace() \n6-Esci \nInserisci opzione: "))
        if opt==1:
            print("len() fornisce la lunghezza di una stringa.")
            print("La lunghezza della frase inserita è", len(s))
        elif opt==2:
            print("upper() converte una stringa in maiuscolo")
            u=s.upper()
            print("Convertiamo la stringa in minuscolo:",u)
        elif opt==3:
            print("lower() converte una stringa in minuscolo")
            l=s.lower()
            print("Convertiamo la stringa in minuscolo:",l)
        elif opt==4:
            print("split() divide una stringa in una lista di sottostringhe in base a un delimitatore.")
            lista=s.split('')
            print("Dividiamo la frase in parole:",lista)  
        elif opt==5:
            print("replace() sostituisce parti di una stringa con un'altra.")
            r=s.replace('a','X')
            print("Sostituiamo le 'a' con le 'X':",r)
        elif opt==6:
            chk=False
        else:
            print("Errore")
    return

def booleani():
    print("Un booleano è un dato che può assumere solo due valori: True e False. Python supporta gli operatori logici per lavalutazione di espressioni booleane.")
    x=int(input("Inserisci un numero: "))
    y=int(input("Inserisci un numero: "))
    z=int(input("Inserisci un numero: "))
    chk=True
    while chk==True:
        opt = int(input("Quale operatore logico vuoi applicare?\n1-and \n2-or \n3-not \n6-Esci \nInserisci opzione: "))
        if opt==1:
            print("and resistuiscce True se entrambe le condizioni sono vere.")
            print("Esempio.\n",x,"<",y,"e",y,">",z,"?:",x<y and y>z)
        elif opt==2:
            print("or resistuiscce True se almeno una delle condizioni è vera.")
            print("Esempio.\n",x,"<",y,"o",z,">",y,"?:",x<y or z>y)
        elif opt==3:
            print("not resistuiscce il valore booleano opposto di ciò che segue.")
            print("Esempio.\n",x,"<",y,"?:",x<y,"\n Opposto: ", not(x<y))
        elif opt==4:
            chk=False
        else:
            print("Errore")
    return

def liste():
    import random
    print("Una lista è una collezione ordinata e modificabile di elementi.")
    n=int(input("Inserisci lunghezza della lista: "))
    l=[]
    for _ in range(n):
        elemento=input("Inserisci elemento nella lista: ")
        l.append(elemento)
    print(l,"è di tipo",type(l))
    chk=True
    while chk==True:
        opt = int(input("Quale metodo vuoi applicare sulla lista?\n1-len() \n2-append() \n3-insert() \n4-remove() \n5-sort() \n6-Esci \nInserisci opzione: "))
        if opt==1:
            print("len() fornisce la lunghezza di una lista.")
            print("La lunghezza della lista inserita è", len(l))
        elif opt==2:
            print("append() aggiunge un elemento alla fine della lista")
            x=input("Inserisci l'elemento da inserire nella lista: ")
            l.append(x)
            print("La nuova lista è",l)
        elif opt==3:
            nc = random.randint(0,len(l)-1)
            print("insert() inserisce un elemento in una posizione specifica.")
            y=input("Inserisci l'elemento da inserire in posizione "+ str(nc)+": ")
            l.insert(nc, y)
            print("La nuova lista è",l)
        elif opt==4:
            nc1 = random.randint(0,len(l)-1)
            print("remove() rimuove un elemento dalla lista.")
            l.remove(l[nc1])
            print("Togliamo l'elemento",l[nc1],"\n La nuova lista è,",l)  
        elif opt==5:
            print("sort() ordina gli elementi della lista.")
        elif opt==6:
            chk=False
        else:
            print("Errore")
    return

def tuple():
    print("Le tuple sono simili alle liste ma immutabili, il che significa che una volta create, non possono essere modificate.")
    return

def variabili():
    chk=True
    while chk==True:
        opt = int(input("Quale variabile vuoi approfondire?\n1-Numeri \n2-Stringhe \n3-Booleani \n4-Liste \n5-Tuple \n6-Esci \nInserisci opzione: "))
        if opt==1:
            numeri()
        elif opt==2:
            stringhe()
        elif opt==3:
            booleani()
        elif opt==4:
            liste()  
        elif opt==5:
            tuple()
        elif opt==6:
            chk=False
        else:
            print("Errore")
    return



## DEFINIZIONE E TIPI DI FLUSSI

#IF-ELSE-ELIF
def if_else_elif():
    chk=True
    while chk==True:
        opt = int(input("Quale blocco vuoi approfondire?\n1-If \n2-Elif \n3-Else \n4-Esci \nInserisci opzione: "))
        if opt==1:
            print("L'istruzione if viene utilizzata per eseguire un blocco di codice se una determinata condizione è vera.")
            n=int(input("Esempio. \nInserisci numero positivo: "))
            if n>0:
                print("La condizione",n,">0 è vera quindi l'istruzione if viene eseguita e stampa questo messaggio.")
        elif opt==2:
            print("L'istruzione else viene usata per definire un blocco di codice da eseguire se le condizioni dell'if risultano false.")
            n=int(input("Esempio. \nInserisci numero: ")) 
            if n>0:
                print("La condizione",n,">0 è vera quindi l'istruzione if viene eseguita e stampa questo messaggio.")   
            else:
                print("Il numero",n,"non è positivo quindi viene eseguito il blocco else.")
        elif opt==3:
            print("L'istruzione elif per specificare ulteriori condizioni da verificare.")
            n=int(input("Esempio. \nn=0")) 
            if n>0:
                print("La condizione",n,">0 è vera quindi viene eseguito il blocco if stampando questo messaggio.")   
            elif n==0:
                print("La condizione",n,"=0 è soddisfatta quindi viene esguito il blocco elif.")
            else:
                print("Il numero",n,"è negativo quindi viene eseguito il blocco else.")
        elif opt==4:
            chk=False
        else:
            print("Errore")

#CICLO WHILE
def ciclo_while():
    print("L'istruzione while viene utilizzata per eseguire un blocco di codice finché una determinata condizione è vera.")
    chk=True
    while chk==True:
        n=int(input("Esempio. \nInserisci numero da 1 a 5: "))
        if 1<=n<=5:
            print("Contiamo quante volte avviene l'iterazione con la condizione che il numero di iterazioni deve essere minore di",n,".")
            nit=0
            print("Verifichiamo se",nit,"<",n)
            while nit<=n:
                print("La condizione è soddisfatta quindi aggiungiamo 1 al numero di iterazioni.")
                nit+=1
                print("Verifichiamo se",nit,"<",n)
            print("Il numero di iterazioni è >",n,", dunque siamo usciti dal ciclo.")
            chk=False
        else:
            print(n,"non è compreso tra 1 e 5")
    return

#CICLO FOR
def ciclo_for():
    print("L'istruzione for viene utilizzata per iterare su una sequenza di elementi (come una lista, una stringa o una tupla) o su un oggetto iterabile.")
    chk=True
    while chk==True:
        opt = int(input("Su quale oggetto vuoi iterare?\n1-Stringa \n2-Lista \n3-Range \n4-Esci \nInserisci opzione: "))
        if opt==1:
           stringa=input("Inserisci parola: ")
           print("Stampiamo ogni lettera della parola.")
           for lettera in stringa:
               print(lettera)
        elif opt==2:
            n=int(input("Inserisci lunghezza della lista: "))
            l=[]
            for _ in range(n):
                elemento=input("Inserisci elemento nella lista: ")
                l.append(elemento)
            print("Stampiamo ogni elemento della lista.")
            for elemento in l:
                print(elemento)
        elif opt==3:
            print("range() è una funzione incorporata in Python che restituisce una sequenza di numeri interi")
            start=int(input("Inserisci il valore di partenza della sequenza: "))
            stop=int(input("Inserisci il valore di fine della sequenza: "))
            step=int(input("Inserisci lo step (differenza tra due valori successivi della sequenza): "))
            print("Dunque stampiamo gli elementi di",range(start,stop,step))
            for i in range(start,stop,step):
                print(i)
        elif opt==4:
            chk=False
        else:
            print("Errore")
    return

#MAIN FLUSSI
def flussi():
    print("Un flusso è un'esecuzione di un blocco di codice in base a determinate condizioni.")
    chk=True
    while chk==True:
        opt = int(input("Quale flusso vuoi approfondire?\n1-If-Elif-Else \n2-Ciclo While \n3-Ciclo For \n4-Esci \nInserisci opzione: "))
        if opt==1:
           if_else_elif()
        elif opt==2:
            ciclo_while()
        elif opt==3:
            ciclo_for()
        elif opt==4:
            chk=False
        else:
            print("Errore")
    return



## MAIN
def riassunto():
    chk=True
    while chk==True:
        opt = int(input("Quale argomento vuoi approfondire?\n1-Introduzione a Python \n2-UML \n3-Variabili \n4-Flussi \n5-Esci \nInserisci opzione: "))
        if opt==1:
           python()
        elif opt==2:
            UML()
        elif opt==3:
            variabili()
        elif opt==4:
            flussi()
        elif opt==5:
            chk=False
        else:
            print("Errore")
    return

riassunto()