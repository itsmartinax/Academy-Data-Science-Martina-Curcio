l=[]

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

maxl=0
if len(l)==0:
    print("Lista vuota")
else:
    for i in range(len(l)):
        if l[i]>maxl:
            maxl=l[i]
    print("Il massimo è", maxl)
    count=0
    while count<len(l):
        count=count+1
    print("Il numero di elementi della lista è", count)
