# ESERCIZIO CICLI
# Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i numeri 
# da n a 0 (compreso), decrementando di 1. Deve potersi ripetere all'infinito.

n = int(input("Inserire numero: "))

X=True
while X==True:
    # Conto alla rovescia
    for i in range(n, -1, -1):
        print(i)
    # Richiesta nuovo numero    
    op = int(input("Inserire un nuovo numero? \n1- sì \n2- no \nScegliere opzione:"))
    if op==1:
        n = int(input("Inserire numero: "))
    elif op==2:
        X=False
    else:
        print("Errore")

