# ESERCIZIO FUNZIONI

# Calcolo area triangolo
def area_triangolo(b, h):
    return (b*h)/2

# Calcolo area quadrato
def area_quadrato(l):
    return l*l

# Calcolo rettangolo
def area_rettangolo(a,b):
    return a*b

# Calcolo area poligoni
def calcoloarea():
    l=[]
    chk=True
    while chk==True:
        # Richiesta calcolo area
        ques = int(input("Di quale poligono vuoi calcolare l'area? \n1-Triangolo \n2-Quadrato \n3-Rettangolo \n4-Esci \nScegliere opzione: "))
        if ques==1:
            b=int(input("Inserire base triangolo: "))
            h=int(input("Inserire altezza triangolo: "))
            at=area_triangolo(b,h)
            l.append(at)
        elif ques==2:
            x=int(input("Inserire lato quadrato: "))
            aq=area_quadrato(x)
            l.append(aq)
        elif ques==3:
            a=int(input("Inserire primo lato rettangolo: "))
            b=int(input("Inserire secondo lato rettangolo: "))
            ar=area_rettangolo(a,b)
            l.append(ar)
        elif ques==4:
            chk=False
        else:
            print("Errore")
    return l

lista=calcoloarea()
print(lista)