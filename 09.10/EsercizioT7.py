# Scrivete un programma che prenda i nomi degli alunni di una classe e i loro voti, quando l’utente scrive media il programma andrà a 
# stampare i nomi di tutti gli alunni e per ogni alunno la media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media: 10


chk=True
id=0
dizionario={}

while chk==True:
    op=int(input("Inserire un nuovo studente? \n1-sì \n2-no \nScegli opzione: "))
    if op==1:
        nome=input("Inserisci nome studente: ")
        n = int(input("Inserisci numero voti da inserire: "))
        voti = []
        for _ in range(n):
            v = int(input("Inserisci voto: "))
            voti.append(v)
        dizionario[id]={'Nome':nome, 'Voti':voti}
        id+=1
    else:
        chk=False

def media():
    for id in dizionario:
        print("Nome:", dizionario[id]["Nome"], ", Media:", sum(dizionario[id]["Voti"])/len(dizionario[id]["Voti"]))

print(dizionario)
media()



