# ESERCIZIO IF-ELSE-ELIF
# Creare un if con else semplice, dentro l'if inserire una struttura di creazione di dati (nome, password, id dato dal sistema a crescere) 
# e nell'else il controllo automatico là dove è presente l'account nel sistema e solo se si passa dall'else concludere lo script

nome = input("Inserire nome: ")
password = input("Inserire password: ")

if nome != "Martina" or password != "visualstudio":
    registra_nome=input("Inserire nome: ")
    registra_password=input("Inserire password: ")
    Id = 1
    print("Nuovo account: Nome:", registra_nome, "Password:", registra_password, "Id:", Id)
else:
    Id = 0
    modifica = int(input("Vuoi modificare l'account [1- sì, 0- no]? "))
    if modifica == 1:
        modifica_nome=input("Inserire nuovo nome: ")
        modifica_password=input("Inserire nuova password: ")
        print("Nuovo account: Nome:", modifica_nome, "Password:", modifica_password, "Id:", Id)
    elif modifica==0:
        print("Continua con le funzionalità")
    else:
        print("Errore")