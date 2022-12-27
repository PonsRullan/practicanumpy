import numpy as np

calif_a=np.genfromtxt('Speculation_Watch_List_(1).csv', 
                      delimiter=';',dtype=str,skip_header=1)

#formato de direccion: numero-calle-censo-council-barrio-postal-comunidad-ciudad
#calle y barrio son alfanumericos y no se corresponden con censo y council
#a efectos de analisis numerico, la agrupacion menor es postal code
#a efectos de analisis detallado, la agrupacion mas adecuada es Council en 
#sustitucion de barriada (NTA)
#Community y Postcode son clasificaciones no redundantes, pero demasiado 
#similares para ser consideradas ambas, lo mismo que sucece con Council y NTA

#intervalo al 95% de confianza del precio medio en Chinatown
chinatown=calif_a[calif_a[:,16]=='Chinatown',0]
chinatownn=np.zeros(len(chinatown))
for i in range(0,len(chinatown)):
    chinatownn[i]=int(chinatown[i])
    
mchinatown=np.mean(chinatownn)
dchinatown=np.std(chinatownn)
print('(',int(mchinatown-(1.96*dchinatown)/np.sqrt(len(chinatown))),',',
        int(mchinatown+(1.96*dchinatown)/np.sqrt(len(chinatown))),')')

#barrios con mas transacciones
repe=[]
cnt=0

for i in range(0, len(calif_a)):
    if calif_a[i,16] not in repe: 
        repe.append(calif_a[i,16])
        cnt += 1
            
barrio=np.full((cnt,2),'barrio',dtype='<U53')
for i in range(0,cnt):
    cont=0
    for j in range (0,len(calif_a)):
        if repe[i]==calif_a[j,16]:
            cont += 1
            barrio[i,0]=repe[i]
            barrio[i,1]=cont

barriord= np.flip(np.argsort(barrio[:,1])) 
baord=np.full((cnt,2),'barrio',dtype='<U53')
for i in range (0,cnt):
    baord[i,0]=barrio[barriord[i],0]
    baord[i,1]=barrio[barriord[i],1]
              
print(baord)
            
#cap rate es la tasa anual de retorno de la inversion de la transaccion
#(supongo que, como aqui, valorada por hacienda), y de la ciudad

#inversiones realizadas por encima y por debajo del cap de la ciudad
mascaro=np.full((len(calif_a),2),'barrio',dtype='<U53')
masbarato=np.full((len(calif_a),2),'barrio',dtype='<U53')
calif_a1=np.zeros((len(calif_a),2))

for i in range(0,len(calif_a1)):
    calif_a1[i,0]=round(float(calif_a[i,1]),2)
    calif_a1[i,1]=round(float(calif_a[i,2]),2)

for i in range(0, len(calif_a1)):
    if calif_a1[i,0]<=calif_a1[i,1]:
        mascaro[i,0]=calif_a[i,12]
        mascaro[i,1]=round((calif_a1[i,1]-calif_a1[i,0]),2)
    else:
        masbarato[i,0]=calif_a[i,12]
        masbarato[i,1]=round((calif_a1[i,0]-calif_a1[i,1]),2)
        
for i in range(0,len(mascaro)):
    mascaro[i,0]=calif_a[i,19]

#pero resulta que en todos los casos se espera una tasa de retorno inferior
#a la de la ciudad (cap borough)
        
print(mascaro)

#total de recaudacion en el nucleo urbano de MN
mn1=calif_a[calif_a[:,19]=='MN',0]
mn2=calif_a[calif_a[:,19]=='MN',2]
mni=np.zeros((len(mn1),1))

for i in range(0,len(mn1)):
    mni[i]=np.round(int(mn1[i])*float(mn2[i]),0)/1000000
         
print(np.sum(mni),'million USD')
  
#calles de Norwood en las que ha habido transacciones
norwood=calif_a[calif_a[:,16]=='Norwood',13]
callerepe=[]
conta=0
for i in range(0,len(norwood)):
    if norwood[i] not in callerepe:
       callerepe.append(norwood[i])
        
print(callerepe)

