'''
creare un programma per la gestione degli studenti di una scuola, 
all'avvio se il db è presente legge i dati da db altrimenti lo crea, 
l'utente puoi inserire studenti e voti all'interno del db
'''

def crea_file(file):
    with open(file,"x") as myfile:
        myfile.write("id-nome-cognome-voti")

def leggi_file(file):
    with open(file,"r") as myfile:
        db=myfile.read()
        return db

def controllo(file):
    try:
        crea_file(file)
        print("File creato")
    except:
        leggi_file(file)

def leggi_studente(file_name):
    try:
        with open(file_name, 'r') as f:
            studenti = f.readlines()
        if studenti:
            print("Lista degli studenti e voti:\n")
            for i in range(1,len(studenti)-1):
                studente_id, nome, cognome, voti = studenti[i].split('-')
                print(f"ID:{studente_id}, Nome: {nome}, Cognome: {cognome}, Voto: {voti}")
        else:
            print("Nessuno studente presente nel file.")
    except FileNotFoundError:
        print(f"Il file '{file_name}' non è stato trovato.")


def creazione_studente():
    nome=input("Inserisci nome studente: ")
    cognome=input("Inserisci cognome studente: ")
    voti = []
    X=True
    while X==True:
        opt=input("Vuoi inserire un nuovo voto? (s/n) ")
        if opt=='s':
            voto=int(input("Inserisci voto: "))
            voti.append(voto)
        else:
            X=False
    return nome,cognome,voti


def aggiungere_studente(file,nome,cognome,voti):
    with open(file, 'r') as f:
        studenti = f.readlines()
        ultimo_studente=studenti[len(studenti)-1]
        studente_id, _, _, _= ultimo_studente.split('-')
        try:
            id=int(studente_id)+1
        except:
            id=0
    with open(file,"a") as myfile:
        myfile.write(f"\n{id}-{nome}-{cognome}-{voti}")
    


def modifica_studente(file,id):
    with open(file, 'r') as f:
        studenti = f.readlines()
    with open(file,'w') as f:
        for i in range(1,len(studenti)-1):
            studente_id, nome, _, _= studenti[i].split('-')
            studente_id=int(studente_id)
            if studente_id==id:
                opt=input("Cosa vuoi modificare: 1-Nome 2-Cognome 3-Voti \nScegli opzione: ")
                if opt==1:
                    nuovo_nome=input("Inserisci nuovo nome: ")
                
                elif opt==2:
                    pass
                elif opt==3:
                    pass
            else:
                pass






'''Finita la prima parte aggiungete al programma la possibilità di modificare voti e alunni'''



controllo("09.12/studenti1.txt")
#aggiungere_studente("09.12/studenti1.txt","Francesco","Rossi",[1,2,10,3])
with open("09.12/studenti1.txt", 'r') as f:
    studenti = f.readlines()
    print(studenti)
