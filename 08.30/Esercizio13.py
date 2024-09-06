# ESERCIZIO TEST
# Chiedi all'utente di inserire una parola e aggiungila a una lista. Chiedi se l'utente desidera ripetere l'operazione aggiungendo un'altra parola,
# poi, alla fine, stampa tutti gli elementi nella lista.

parole = []
X=True
while X==True:
    op = int(input("Inserire una parola? \n1- sì \n2- no \nScegliere opzione:"))
    if op==1:
        p = input("Inserire parola: ")
        parole.append(p)
    elif op==2:
        X=False
    else:
        print("Errore")
print("La lista è", parole)