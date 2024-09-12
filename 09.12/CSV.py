""" def scrittura_file(file,stringa):
    with open(file,"a") as myfile:
        myfile.write(stringa)


# LEGGERE FILE
contenuto =lettura_file("testCsv.txt")

# DIVIDE LE RIGHE
righe = contenuto.split("\n")
print(righe) 

# DIVIDE OGNI PAROLA DELLA RIGA
for i in range(1,len(righe)):
    print(righe[i].split(",")[0]) """

## AGGIUNGERE NUOVA RIGA
def scrittura_file(file,stringa):
    with open(file,"a") as myfile:
        myfile.write(stringa)

nome="giovanni"
cognome="rossi"
via="via roma"

stringa="\n"+nome+","+cognome+","+via
scrittura_file("09.12/file.csv",stringa)
