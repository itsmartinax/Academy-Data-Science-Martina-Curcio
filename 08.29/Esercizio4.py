# ESERCIZIO IF-ELSE-ELIF
# Devi scrivere un programma Python che simuli un sistema di login. Il sistema deve permettere all'utente 
# di inserire un nome utente e una password. Poi, deve verificare se la combinazione di nome utente e 
# password è corretta. Per semplicità, puoi hardcodare nel codice una coppia di nome utente e password 
# che sia considerata corretta. Requisiti:
# 
# 1. Input dell'utente:
# - Il programma chiede all'utente di inserire la password.
# - Poi, chiede all'utente di inserire la password.
#
# 2. Verifica delle credenziali:
# - Il programma controlla se il nome utente e la password inseiriti corrispondono a quelli predifiniti.
# - Puoi decidere di avere le credenziali hardcoded nel codice per questo esercizio. Ad esempio,
#   puoi usare "admin" come nome utente e "12345" come password.
#
# 3. Output del programma:
# - Se il nome utente e la password sono corretti, stampa un messaggio di benvenuto.
# - Altrimenti, informa l'utente che le credenziali sono errate.
#
# 4. Modifica dati del programma:
# - Inserisci una condizione interna che si occupi di cambiare un dato specifico tra quelli inseriti
# - Appena loggato fai scegliere fra due opzioni di domanda segreta e la risposta (qual è il colore
#   preferito, quale animale preferito)


# Inserimento nome utente
nome_utente = input("Inserisci nome utente: ")
# Inserimento password
password = input("Inserisci password: ")

nome_utente_predefinito = "admin"
password_predefinita = "12345"

# Se il nome utente e la password sono corretti si stampa il messaggio di benvenuto 
if nome_utente == nome_utente_predefinito and password == password_predefinita :
    print("Benvenuto/a", nome_utente)
    
    # Si chiede quale modifica si vuole compiere
    opt = int(input("Vuoi modificare le credenziali? \n0 - Nome utente, \n1 - Password, \n2 - Nessuna modifica \nScegli un'opzione: "))

    # Modifica nome utente
    if opt==0:
        nuovo_nome_utente = input("Inserisci nuovo nome utente: ")
        print("Procedi con le funzionalità")

    # Modifica password
    elif opt==1:
        nuova_password = input("Inserisci nuova password: ")

        # Si chiede se si vuole aggiungere una domanda di sicurezza 
        ques = int(input("Vuoi inserire domanda di sicurezza? \n0 - Qual è il tuo colore preferito?, \n1 - Qual è il tuo animale preferito?, \n2 - Nessuna domanda \n Scegli un'opzione: "))
        # Aggiungere risposta alla domanda di sicurezza
        if ques == 0:
            colore = input("Inserisci colore preferito: ")
            print("Procedi con le funzionalità")
        elif ques == 1:
            animale = input("Inserisci animale preferito: ")
            print("Procedi con le funzionalità")
        elif ques == 2:
            print("Procedi con le funzionalità")
        else:
            print("Nessuna opzione selezionata è valida")

    elif opt==2:
        print("Procedi con le funzionalità")
    else:
        print("Nessuna opzione valida selezionata")

# Se le credenziali sono errate si stampa un messaggio di errore 
else:
    print("Credenziali errate")
