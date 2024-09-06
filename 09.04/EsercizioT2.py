# Creare un programma che genera una lista da 10 input dell'utente, dovrà restituire il numero medio, il numero massimo e il numero minimo

l=[]
for i in range(10):
    n=float(input("Inserire numero: "))
    l.append(n)

print(l)

maxl=l[0]
minl=l[0]
sum=0
for i in l:
    if i > maxl:
        maxl=i
    elif i < minl:
        minl=i

l.sort()
medl = l[4]+l[5]
    
print(l)
print("Il numero massimo è", maxl)
print("Il numero minimo è", minl)
print("I numeri medi sono", medl/2)

