# ESERCIZIO IF-ELSE-ELIF
# Creare una serie di condizioni una dentro l'altra che a fronte di un input per ogni if decidano se farti passare o no 
# (3 livelli, fare un paragone con ==)

b = int(input("Inserire numero: "))

if b%2 == 0:
    print(b, "è pari")
else:
    print("b è dispari")
    a = int(input("Inserire numero: "))
    if b%a == 0:
        print(b, "è multiplo di", a)
        c = int(input("Inserire numero: "))
        if a%c == 0: 
            print(a, "è multiplo di", c)
        else:
            print(a, "non è multiplo", c)
    else:
        print(b, "non è multiplo di", a)