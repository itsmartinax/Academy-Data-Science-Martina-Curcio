""" lista=[1,2,3,4,5,6,7,8,9,10]
print(lista[7:1:-1])
i = lista.index(9)
print(i)
stringa="ciao a tutti"
print(stringa.startswith('ciao'))
print(stringa.endswith('t'))
print(stringa.isalnum())
print(stringa.isalpha())
print(stringa.isdecimal())
print(stringa.count('o')) """

# stringa="ciao a tutti"
# lista=stringa.split(" ")
# print(lista)

# separatore="-"
# stringa1=separatore.join(lista)
# print(stringa1)

# if 'ci' in lista:
#     print("si")
# else:
#     print('no')

lista2=['ciao', 'a', 'tutti', 'bianco', 'blu']
lista3=[parola for parola in lista2 if "a" not in parola]
print(lista3)