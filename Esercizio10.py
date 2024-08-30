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

