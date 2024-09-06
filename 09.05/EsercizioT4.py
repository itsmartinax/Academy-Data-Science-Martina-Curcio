# Scrivete una programma che richiede una lista di numeri all’utente e fornisce in output un istogramma basato su questi numeri, usando asterischi
# per disegnarlo.

n=int(input("Scegliere lunghezza della lista: "))
l=[]
for i in range(n):
    x=int(input("Inserire numero: "))
    l.append(x)
ist=[]
for i in l:
    ist=[]
    for j in range(i):
        ist.append('-')
    stringa =''.join(ist)
    print(stringa)