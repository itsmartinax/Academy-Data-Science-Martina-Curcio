# ESERCIZIO CICLI
# Scrivi un sistema che prende in input una lista di numeri interi che precedentemente è stata valorizzata dall'utente.
# Il sistema deve:
# 1. Utilizzare un ciclo for per trovare il numero massimo della lista.
# 2. Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
# 3. Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, altrimenti stampare il numero massimo
#    trovato e il numero di elementi nella lista.

l=[]

# Creazione della lista
X=True
while X==True:
    op = int(input("Inserire un nuovo numero? \n1- sì \n2- no \nScegliere opzione:"))
    if op==1:
        n = int(input("Inserire numero: "))
        l.append(n)
    elif op==2:
        X=False
    else:
        print("Errore")
print("La lista è", l)

# Verifica lista vuota
maxl=0
if len(l)==0:
    print("Lista vuota")
else:
    # Ciclo for per trovare il massimo della lista
    for i in range(len(l)):
        if l[i]>maxl:
            maxl=l[i]
    print("Il massimo è", maxl)
    count=0
    # Ciclo while per trovare il numero degli elementi della lista
    while count<len(l):
        count=count+1
    print("Il numero di elementi della lista è", count)
