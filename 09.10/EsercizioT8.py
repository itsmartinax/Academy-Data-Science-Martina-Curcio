# Scrivete un programma che utilizza una funzione che accetta come parametro una stringa passata dall’utente e restituisce in
# risposta se è palindroma o no.
# Esempio:
#‘I topi non avevano nipoti’ è palindroma
#'ciao' non è palindroma

stringa="Angolo bar a Bologna"
stringa2="ciao a tutti"


def palindromo(stringa):
    s=stringa.lower()
    s=s.replace(" ","")
    s=s.replace(",","")
    s=s.replace("è","e")
    chk=True
    for i in range(int(len(s)/2)):
        if s[i]!=s[len(s)-1-i]:
            return False
    return True

    #         chk=False
    # if chk==True:
    #     print(stringa, "è palindroma")
    # else:
    #     print(stringa, "non è palindroma")

print(palindromo(stringa2))

    

