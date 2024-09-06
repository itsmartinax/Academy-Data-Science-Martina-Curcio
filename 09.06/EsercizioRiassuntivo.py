 # ESERCIZIO RIASSUNTIVO

def UML():
    print("L'UML è un linguaggio standardizzato per la modellizazione di software.")
    chk=True
    while chk==True:
        opt = int(input("Cosa vuoi sapere?\n1-Caratteristiche \n2-Elementi fondamentali \n3-Esci \nInserisci opzione: "))
        if opt==1:
            print("1. Standardizzato: \n Le sue specifiche sono uniformi e riconosciute a livello internazionale. \n2. Visuale: \n Utilizza diagrammi per rappresentare gli elementi e le relazioni in un sistema software. \n3. Polivalente: \n Modella sistemi di vario tipo. \n4. Estensibile: \n Permette la personalizzazione delle regole a patto che le nuove siano coerenti con le precedenti.")
        elif opt==2:
            print("1. Strutture statiche: \n Elementi irremovibili che rappresentano gli obblighi che hanno macchina e utente. \n2. Comportamenti dinamici: \n Azioni pratiche che variano nel tempo. \n3. Aspetti di organizzazione: \n Insieme delle regole comuni con cui si visualizza l'UML, anche dette stereotipi.")
        elif opt==3:
            chk=False
        else:
            print("Errore")
    return

def cicli():
    print("Un flusso è un'esecuzione di un blocco di codice in base a determinate condizioni.")
    chk=True
    while chk==True:
        opt = int(input("Quale flusso vuoi approfondire?\n1-If-Elif-Else \n2- Ciclo While \n3- Ciclo For \n4-Esci \nInserisci opzione: "))
        if opt==1:
            opt1 = int(input("Quale comando vuoi approfondire?\n1-If \n2-Elif \n3-Else \n4-Esci \nInserisci opzione: "))
        elif opt==2:
            pass
        elif opt==3:
            pass
        elif opt==4:
            chk=False
        else:
            print("Errore")
    return

