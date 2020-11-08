#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, 
#pentru intervalul de la a la b (a și b se citesc de la tastatură).
a=int(input("Dati a:"))
b=int(input("Dati b:"))
for i in range(a,b):
    if (i%2!=0):
        print(i, end=' ')
