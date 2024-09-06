# Creare un programma che genera una lista da 10 input dell'utente, dovrà restituire il numero medio, il numero massimo e il numero minimo

l=[]
for i in range(10):
    n=float(input("Inserire numero: "))
    l.append(n)

for i in range(len(l)):
    for j in range(len(l)):
        if i<j and l[i]>l[j]:
            m=l[i]
            l[i]=l[j]
            l[j]=m

print(l)
maxl=l[len(l)-1]
minl=l[0]
medl = l[4]+l[5]

print("Il numero massimo è", maxl)
print("Il numero minimo è", minl)
print("I numeri medi sono", medl/2)