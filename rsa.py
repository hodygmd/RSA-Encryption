
import numpy as np
#print('¿cuantos caracteres contiene el mensaje?')
print('Escribir el mensaje: ',end='')
frase=input()
letras=frase.upper()
m=np.zeros((len(letras)))
c=np.zeros((len(m)))

maux='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#for i in range(0,len(m)):
#    print('Ingresar caracter',i+1,': ',end='')
#    m[i]=input()

for i in range(0,len(m)):
    for j in range(0,len(maux)):
        if letras[i]==maux[j]:
            m[i]=j  
print(m)
print()
print('Ingresar valor de p: ',end='')
p=input()
print('Ingresar valor de q: ',end='')
q=input()
print('Ingresar valor de e: ',end='')
e=input()
print()
eaux=int(e)
n=int(p)*int(q)
z=(int(p)-1)*(int(q)-1)
d=0
for i in range(1,z):
    if (eaux%z)*(i%z)%z==1:
        d=i

print('Clave publica(',eaux,',',n,')')
print('Clave privada(',d,',',n,')')
print()
for i in range(0,len(m)):
    c[i]=m[i]**eaux%n
    print(m[i],'^',eaux,'mod',n,'=',c[i])