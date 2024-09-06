import random
n=random.randint(1, 5) 

def Gioco(n):
    chk=True
    while chk==True:
        ques = int(input("Vuoi inserire un nuovo numero? \n1-sì \n2-no \nScegliere opzione:"))
        if ques==1:
            x = int(input("Inserisci numero: "))
            if n==x:
                print("Il numero da indovinare è", x)
                chk=False
                break
            elif n<x:
                print("Il numero da indovinare è più basso di", x)
                Gioco(n)
            else:
                print("Il numero da indovinare è più alto di", x)
                Gioco(n)
        else:
            print("Gioco terminato")
            chk=False

Gioco(n)