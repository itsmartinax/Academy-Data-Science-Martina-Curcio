n = int(input("Inserire numero: "))
l=[]

chk=True
while len(l)<6:
    for i in range(2, int(n/2)+1):
        if n%i==0:
            print(n, "non è primo")
            chk = False
            break
    if chk==True:
        print(n, "è primo")
        l.append(n)
    n = int(input("Inserire numero: "))
    chk=True