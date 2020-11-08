#Să se calculeze sumele: 	
#s1=1+2+3+…+n    s2=1*2+2*3+3*4+…+(n-1)*n   s3=1+1*2+1*2*3+…+1*2*3*…*n
#s4=12+22+32+…+n2   s5=1/2+2/3+3/4+…+n/(n+1)   s6=1+2+22+23+24+…+2n
#Notă: Pentru fiecare sumă n – se va citi de la tastatură.
n=int(input("Dati n:"))
s1=0
s2=0
s3=0
s4=0
s5=0
s6=1
p=1
for i in range(1,n+1):
    s1+=i
    s2+=(i-1)*i
    p*=i
    s3+=p
    s4+=(10*i)+2
    s5+=i/(i+1)
    s6+=int('2'+str(i))

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)