# ESERCIZIO IF-ELSE-ELIF
# Andare a creare un if con vari elif e un else finale che gestisca un menu per la selezione di un crud basilare (aggiungi rimuovi elimina)
# su una lista di stringhe

s = input("Inserisci una parola: ")
o = input("Quale operazione vuoi compiere tra aggiungere, modificare o eliminare: ")

if o == "aggiungere":
    t=input("Inserire la parola da aggiungere: ")
    print("Nuova stringa", s, t)
elif o == "modificare":
    u=input("Inserire la nuova parola: ")
    s=u
    print("Nuova parola:", s)
elif o=="eliminare":
    s=""
    print(s)
else:
    print("Nessuna operazione valida")
