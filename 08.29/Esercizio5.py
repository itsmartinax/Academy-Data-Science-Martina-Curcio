# ESERCIZIO IF-ELSE-ELIF
# Scrivi un programma che chieda all'utente la sua età. Se l'età è inferiore a 18 anni, il programma dovrebbe stampare 
# "Puoi vedere questo film". Altrimenti dovrebbe stampare "Puoi vedere questo film".

# Inserimento dell'età
età = int(input("Inserisci la tua età: "))

# Controllo dell'età
if età < 18:
    print("Mi dispiace, non puoi vedere questo film")
else:
    print("Puoi vedere questo film")