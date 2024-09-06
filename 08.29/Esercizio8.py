# ESERCIZIO RANGE
# Il programma dovrebbe controllare se il numero inserito è primo o no. Se è primo, lo salva e stampa "Il numero è primo".
# Altrimenti, stampa "Il numero non è primo". Si ferma il tutto quando ha 5 numeri primi.

l=[]
chk=True
while len(l)<5:
    n = int(input("Inserire numero: "))
    
    # Controllo se il numero è primo
    for i in range(2, int(n/2)+1):
        if n%i==0:
            print(n, "non è primo")
            chk = False
            break
    if chk==True:
        print(n, "è primo")
        l.append(n)

    # Ripristina il controllo a True per il prossimo numero
    chk=True 

print(l)