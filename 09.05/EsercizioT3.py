# Scrivete un programma che chiede all'utente una frase e restituisce solo le vocali e l’indice della vocale all’interno della frase.

frase = input("Inserisci una frase: ")
lista=list(frase)
vocali=['a','e','i','o','u']
print(lista)
count=0
for char in lista:
    if char in vocali: 
        print(char, count)
    count+=1