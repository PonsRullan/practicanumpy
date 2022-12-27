import numpy as np

eu2D=np.loadtxt('europa20.csv',dtype=None,delimiter=';',skiprows=1,
                usecols=np.arange(1,56))
eutotal=np.loadtxt('europa20.csv',dtype=None,delimiter=';',skiprows=1,
                  usecols=(1,2,3,4,5,6,7,8,9,10,11))
eucentral=np.loadtxt('europa20.csv',dtype=None,delimiter=';',skiprows=1,
                  usecols=(12,13,14,15,16,17,18,19,20,21,22))
eufederal=np.loadtxt('europa20.csv',dtype=None,delimiter=';',skiprows=1,
                  usecols=(23,24,25,26,27,28,29,30,31,32,33))
eulocal=np.loadtxt('europa20.csv',dtype=None,delimiter=';',skiprows=1,
                  usecols=(34,35,36,37,38,39,40,41,42,43,44))
eusocial=np.loadtxt('europa20.csv',dtype=None,delimiter=';',skiprows=1,
                  usecols=(45,46,47,48,49,50,51,52,53,54,55))
#esta tabla nos servira para identificar paises "string" por su indice numerico
paises=np.loadtxt('europa20.csv',dtype=str,delimiter=';',skiprows=1, 
                  usecols=(0,56))

euro=np.array([eutotal,eucentral,eufederal,eulocal,eusocial])
print(euro.shape)

#ahora tenemos un tensor (5,30,11) 
#       4: en su conjunto y gobiernos central, federal, local, social
#       30 países europeos
#       el gasto en porcentaje sobre el PIB en su conjunto y para cada gob: 
#       10 partidas de gasto (administracion, militar, policia, economia, 
#       medio ambiente, infraestructuras, salud, cultura, educacion, social)

#Gasto en educacion de los paises ordenados segun su esfuerzo fiscal total
euord=np.flip(np.argsort(euro[0,:,0]))

poeduc=np.full((30,2),'valor',dtype='<U53')
for i in range(0,30):
    poeduc[i,0]=paises[euord[i],0]
    poeduc[i,1]=euro[0,euord[i],9]
print(poeduc)  
  
#Gasto social de las autonomias en los paises con estructura federal 
p1=paises[euro[2,:,0]!= 0,0]
e1=euro[2,euro[2,:,0]!= 0,10]
gs=np.full((5,2),'gasto',dtype='<U53')
for i in range (0,5):
    gs[i,0]=p1[i]
    gs[i,1]=e1[i]

print(gs)

#gasto agregado de educacion, salud y pensiones en los paises ordenados 
#segun el gasto en fuerzas policiales y militares 
mp=np.flip(np.argsort(euro[0,:,2]+euro[0,:,3]))
ss=euro[0,mp[:],7]+euro[0,mp[:],9]+euro[0,mp[:],10]
pm=np.full((30,2),'gasto',dtype='<U53')
for i in range (0,30):
    pm[i,0]=paises[mp[i],0]
    pm[i,1]=ss[mp[i]]
    
print(pm)

#paises en los que los ayuntamientos dedican mas porcentaje de gasto a cultura
#que el gobierno central
rati=euro[3,:,8]/euro[1,:,8]
ratiord=np.flip(np.argsort(rati[:]))
k=0
gc=np.zeros((30,2))
for i in range (0,30):
    gc[i,0]=ratiord[i]
    gc[i,1]=rati[ratiord[i]]
    if gc[i,1]<1:
        k=k+1
        
gca=np.full((30-k,2),'cultura',dtype='<U53')
for i in range(0,30-k):
    gca[i,0]=paises[int(gc[i,0]),0]
    gca[i,1]=gc[i,1]

print(gca)

#paises con pensiones saneadas (sin costes financieros de deuda)
ssps=paises[euro[4,:,4]== 0,0]

print('paises con SS saneada:', ssps)

sspns=paises[euro[4,:,4]!= 0,0]
ssg=euro[4,euro[4,:,4]!= 0,4]
ssgord=np.flip(np.argsort(ssg))

ss=np.full((len(ssgord),2),'ss',dtype='<U53')
for i in range (0,len(ssgord)):
    ss[i,0]=sspns[ssgord[i]]
    ss[i,1]=ssg[ssgord[i]]
    
print('paises con SS financiada:',ss)