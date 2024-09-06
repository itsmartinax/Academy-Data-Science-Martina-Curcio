# ESERCIZIO IF-ELSE-ELIF
# Scrivi un programma che chieda all'utente di inserire due numeri e un'operazione da eseguire tra (+), sottrazione (-), moltiplicazione (*)
# e divisione (/). Il programma poi dovrebbe eseguire l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere per zero, 
# il programma dovrebbe stampare "Errore: Divisione per zero". Se l'operazione inserirta non è riconosciuta, dovrebbe stampare 
# "Operazione non valida"

# Inserire i numeri
x = float(input("Inserire numero: "))
y = float(input("Inserire numero: "))

# Inserire operazione
op = int(input("\n1- + \n2- - \n3- * \n4- / \n Scegliere operazione: "))

# Eseguire operazione
if op==1:
    print("La somma tra ", x, "e", y, "è", x+y)
elif op==2:
    print("La sottrazione tra ", x, "e", y, "è", x-y)
elif op==3:
    print("La moltiplicazione tra ", x, "e", y, "è", x*y)
elif op==4:
    if y==0:
        print("Errore: divisone per 0")
    else:
        print("La divisione tra ", x, "e", y, "è", x/y)
else:
    print("Operazione non valida")