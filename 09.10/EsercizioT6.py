# Scrivete un programma che chiede un numero all’utente e restituisce un dizionario con il quadrato del numero, se è pari o dispari 
# e quante cifre contiene.
# Esempio:
# Numero 12
# Risultato
# {‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }

n=int(input("Inserisci numero: "))

dizionario={}

dizionario['quadrato']=n**2

if n%2==0:
    dizionario['pari o dispari']='pari'
else:
    dizionario['pari o dispari']='dispari'

dizionario['n. cifre']=len(str(n))

print(dizionario)



# n=int(input("Inserisci numero: "))

# dizionario={'quadrato':[],'pari o dispari':[],'n.cifre':[]}

# dizionario['quadrato'].append(n**2)

# if n%2==0:
#     dizionario['pari o dispari'].append('pari')
# else:
#     dizionario['pari o dispari'].append('dispari')

# dizionario['n. cifre'].append(len(str(n)))

# print(dizionario)