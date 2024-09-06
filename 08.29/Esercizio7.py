# ESERCIZIO CICLI
# Chiedi all'utente di inserire un numero. Il programma dovrebbe quindi fare un conto alla rovescia a partire da quel numero fino a zero, 
# stampando ogni numero e chiederti se vuoi ripetere. Chiedi all'utente di inserire un numero.


n = int(input("Inserire numero: "))

X=True
while X==True:
    # Conto alla rovescia
    for i in range(n+1):
        print(n-i)
    # Richiesta nuovo numero    
    op = int(input("Inserire un nuovo numero? \n1- sì \n2- no \nScegliere opzione:"))
    if op==1:
        n = int(input("Inserire numero: "))
    elif op==2:
        X=False
    else:
        print("Errore")
    
