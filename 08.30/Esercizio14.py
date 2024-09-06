# ESERCIZIO TEST
# Chiedi all'utente due liste di 5 numeri ciascuna, poi stampa le somme degli elementi che si trovano negli stessi indici. 
# Infine, chiedi se vogliono ripetere l'operazione.

X=True
while X==True:
    # Richiesta se si vogliono inserire le liste
    op = int(input("Inserire nuove liste? \n1- sì \n2- no \nScegliere opzione:"))
    if op==1:
        l1 = []
        l2 = []
        # Lista 1
        for i in range(5):
            n = int(input("Inserisci numero della Lista 1: "))
            l1.append(n)
        # Lista 2
        for i in range(5):
            n = int(input("Inserisci numero della Lista 2: "))
            l2.append(n)
        print("Lista 1:", l1, "\nLista 2:", l2)
        s = []
        # Somme degli elementi che si trovano negli stessi indici
        for i in range(5):
            m = l1[i]+l2[i]
            s.append(m)
        print("Somme degli elementi che si trovano negli stessi indici:", s)
    elif op==2:
        X=False
    else:
        print("Errore")





