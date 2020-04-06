import numpy as np
from random import randint, uniform,random
#randint
import matplotlib.pyplot as plt
ale = np.random.normal(0,3,10)
#print(ale)
k = randint(0,10)
#print(k)
val=100001
j =uniform(0,10)
print(j)
a = np.arange(13)
#print(len(a))conda install -c anaconda numpy
for i in range(0,12):
            a[i]=0
            #print(a[i])
for m in range(0,val):
        cont = randint(0,12)
        dado1= int(randint(1,6)*0.8)+1
        dado2= int(randint(1,6)*0.8)+1
        aux=int((dado1+dado2))
        a[cont]=aux
resultado=[]
for p in range(2,13):
        resultado.append(a[p]*val)
        print(str(p)+"   "+str(a[p]*val))
xx=range(2,len(resultado)+2)
plt.bar(xx,resultado,width=0.5,color='blue',align='center')
plt.ylabel('Suma de llos 2 dados'+' con la libreria RandInt')
plt.xlabel('Probabilidad de exito')
plt.show()