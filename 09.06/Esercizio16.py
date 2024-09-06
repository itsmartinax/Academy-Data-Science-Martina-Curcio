#n = int(input("Inserisci numero: "))

def Fibonacci(n):
    l=[1,1]
    i=1
    chk=True
    while l[i]<n:
        f=l[i]+l[i-1]
        l.append(f)
        i+=1
    l.pop()
    return(l)

l=Fibonacci(50)
print(l)
