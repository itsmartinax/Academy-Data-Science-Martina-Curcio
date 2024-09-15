import pickle
""" dizionario ={1:"Martina",2:"Curcio"}
dizB=pickle.dumps(dizionario)

with open("binario.bin","wb") as myfile:
    myfile.write(dizB) """

''' with open("09.12/binario.bin","rb") as myfile:
    contenuto=myfile.read()

contenuto=pickle.loads(contenuto)
print(contenuto) '''


class gatto:
    def __init__(self,nome,razza):
        self.nome=nome
        self.razza