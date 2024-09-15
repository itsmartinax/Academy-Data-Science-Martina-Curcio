import mysql.connector

# Serve per connettere lo script con il server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=8889,
    database="SQLpython" #aggiungere per connettersi al singolo db
)

# Serve per interagire con il server
mycursor=mydb.cursor() 

# Creo un nuovo database
# sql = "create database SQLPython" #Query
""" 
sql="show databases"
mycursor.execute(sql)

for db in mycursor:
    print(f"database:{db}") """

# sql="create table utenti(id int auto_increment primary key, nome varchar(255), cognome varchar(255))"

# inseriamo %s in modo che siano dinamiche 

def inserisci_utente():
    sql = "insert into utenti(nome,cognome) values(%s,%s)"
    val=[("giovanni","rossi"),("francesco","ferrari"),("luca","verdi")] # si può inserire una lista di valori
    mycursor.executemany(sql,val)
    mydb.commit() #permette di inserire o modificare i dati in un database
    print(mycursor.rowcount,"record inseriti") # rowcount conta le righe

sql = "select * from utenti where id > 3"

mycursor.execute(sql)

dati = mycursor.fetchall() # Cattura gli elementi dal cursore 
for dato in dati:
   print(dato)

mycursor.execute(sql) # bisogna sempre eseguire la query prima perché fetchall togli gli elementi dal cursore
dati1 = mycursor.fetchone() # prende una sola riga del risultato
print(dati1)



def delete():
    sql="delete from utenti where id=4"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,"righe eliminate")