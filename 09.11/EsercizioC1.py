# ESERCIZIO CLASSI
''' Crea una classe chiamata Punto. Questa classe dovrebbe avere:

Due attributi: x e y, per rappresentare le coordinate del punto nel piano.

Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le
coordinate del punto di questi valori.

Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del
piano. '''

class Punto:
    
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def muovi(self, dx, dy):
        self.x=self.x+dx
        self.y=self.y+dy
        print("I nuovi punti sono:",(self.x, self.y))
    
    def distanza_da_origine(self):
        distanza=self.x**2 + self.y**2
        print("La distanza al quadrato è",(self.x,self.y),"da (0,0) è", distanza)

        
Punto1=Punto(3,5)
Punto2=Punto(-2,0.5)

Punto1.muovi(0,4)
Punto2.distanza_da_origine()