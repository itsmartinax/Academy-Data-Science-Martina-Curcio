# ESERCIZIO IF-ELSE-ELIF
# Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari e "Dispari" se il numero è dispari.

n=int(input("Inserisci un numero: "))

X=True
while X==True:
    if n%2 == 0:
        print(n, "è pari")
    else:
        print(n, "è dispari")
    op = int(input("Vuoi inserire un altro numero? \n1-sì \n2-no \nScegli opzione:"))
    if op==1:
        n=int(input("Inserisci un numero: "))
    elif op==2:
        X=False
    else:
        print("Errore")

print("Operazione terminata")
        
