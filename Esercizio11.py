m = int(input("Inserire la lunghezza della lista: "))
l=[]
q=[]

for i in range(m):
    n = float(input("Inserire numero: "))
    l.append(n)
print(l)

for j in l:
    n2 = j**2
    q.append(n2)
    print("Il quadrato di", j, "è", n2)

print(q)


