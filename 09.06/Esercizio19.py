# ESERCIZIO DEF-DECORATORI

def controllo(comprimi_stringa):
    def wrapped(s):
        t=comprimi_stringa(s)  
        if len(s)<len(t):
            return s
        else:
            return t 
    return wrapped

@controllo
def comprimi_stringa(s):  
    count=1
    t=''
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            t=t+str(s[i-1])+str(count)
            count=1
    t=t+str(s[i-1])+str(count)
    return t

s=input("Inserisci stringa: ")
print(comprimi_stringa(s))






