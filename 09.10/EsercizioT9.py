'''Scrivete un programma che utilizza il cifrario di Cesare per criptare una
parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
di posti corrispondente alla chiave. '''


def cifrario(alfabeto, chiave):
    alfabeto2=2*alfabeto
    cifrario={}
    cifrario_inverso={}
    for i in range(len(alfabeto)):
        cifrario[alfabeto[i]] = alfabeto2[i+chiave]
        cifrario_inverso[alfabeto2[i+chiave]] = alfabeto[i]
    return cifrario, cifrario_inverso
    
def criptare(stringa, cifrario):
    s_criptata = ""
    for char in stringa:
        if char==" ":
            s_criptata += char
        else:
             s_criptata += cifrario[char]
    return s_criptata

def decriptare(stringa, cifrario_inverso):
    s_decriptata = ""
    for char in stringa:
        if char==" ":
            s_decriptata += char
        else:
             s_decriptata += cifrario_inverso[char]
    return s_decriptata


alfabeto="abcdefghilmnopqrstuvz"
chiave=3
cifrario, cifrario_inverso = cifrario(alfabeto, chiave)
print(cifrario)
print(cifrario_inverso)

stringa='ciao sono martina'
sc=criptare(stringa, cifrario)
print(sc)
sd=decriptare(sc,cifrario_inverso)
print(sd)

# chk=True
# while chk==True:
#     chiave=int(input("Inserisci chiave: "))
#     cifrario, cifrario_inverso = cifrario(alfabeto, chiave)
#     opt=input("Cosa vuoi fare? \n1-Criptare \n2-Decriptare \n3-Esci \nScegli una opzione:")
#     if opt==1:
#         stringa=input("Inserisci stringa: ")
#         criptare(stringa, cifrario)
#     if opt==2:
#         stringa=input("Inserisci stringa: ")
#         decriptare(stringa,cifrario_inverso)
#     else:
#         chk=False
