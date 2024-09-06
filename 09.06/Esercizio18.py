# def primo(n):    
#     chk=True
#     for i in range(2, n):
#         if n%i==0:
#             chk = False
#     if chk==True:
#         return True
#     else:
#         return False

def primo_o_no(funzione):
    def wrapped():
        n=funzione()
        chk=True
        for i in range(2, n):
            if n%i==0:
                chk = False
        if chk==True:
            return n, True
        else:
            return n, False
    return wrapped

@primo_o_no
def num():
    # nome = input("Inserire nome: ")
    n=int(input("Inserire numero: "))
    return n

n, test = num()

def primodivisore(n):
    for i in range(2,n):
        if n%i==0:
            print("Il primo divisore di",n,"è",i)
            break

def funzione():
    l=[]
    test = True
    while test==True:
        n, test = num()
        if test==True:
            l.append(n)
    primodivisore(n)
    return l

print(funzione())
