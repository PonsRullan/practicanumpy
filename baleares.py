import numpy as np

balear=np.genfromtxt('balears.csv', delimiter=';',dtype=str,skip_header=1)
balear1=np.asarray(balear)
lon=len(balear1)//5
#Series por nacidos vivos por residencia materna
nvrm=balear1[balear1[:,1]=='nacidos vivos por residencia materna',2]
#Serie por matrimonios
mlfr=balear1[balear1[:,1]=='matrimonios por el lugar en que han fijado residencia',2]
#Serie por muertes fetales
mftrm=balear1[balear1[:,1]=='muertes fetales tardÃ\xadas por residencia materna',2]
#Serie ordenada por fallecidos por el lugar de residencia
cpflr=np.full((lon,2),'valor',dtype='<U53')
flr=balear1[balear1[:,1]=='fallecidos por el lugar de residencia',0]
cpflr[:,0]=np.char.ljust(flr,5)
cpflr[:,1]=balear1[balear1[:,1]=='fallecidos por el lugar de residencia',2]
#Serie por crecimiento vegetativo
cv=balear1[balear1[:,1]=='crecimiento vegetativo',2]

#al pasar a entero, me da un error por usar punto como separador de miles en Palma
nvrm1=nvrm.astype(float) 
nvrm2=np.zeros(len(nvrm1),dtype=int)
for i in range(0,len(nvrm1)):
    
    if nvrm1[i]*1000%1000==0:
        nvrm2[i]=nvrm1[i]     
    else:
        nvrm2[i]=nvrm1[i]*1000  
mlfr1=mlfr.astype(float)
mlfr2=np.zeros(len(mlfr1),dtype=int)
for i in range(0,len(mlfr1)):
    
    if mlfr1[i]*1000%1000==0:
        mlfr2[i]=mlfr1[i]     
    else:
        mlfr2[i]=mlfr1[i]*1000  
mftrm1=mftrm.astype(float) 
mftrm2=np.zeros(len(mftrm1),dtype=int)
for i in range(0,len(mftrm1)):
    
    if mftrm1[i]*1000%1000==0:
        mftrm2[i]=mftrm1[i]     
    else:
        mftrm2[i]=mftrm1[i]*1000  
cpflr1=cpflr.astype(float)
cpflr2=np.zeros((len(cpflr1),2),dtype=int)
for i in range(0,len(cpflr1)):
      
    if cpflr1[i,1]*1000%1000==0:
        cpflr2[i,1]=cpflr1[i,1]
        cpflr2[i,0]=cpflr1[i,0]
    else:
        cpflr2[i,1]=cpflr1[i,1]*1000
        cpflr2[i,0]=cpflr1[i,0]
    
cv1=cv.astype(float)
cv2=np.zeros(len(cv1),dtype=int)
for i in range(0,len(cv1)):
    
    if cv1[i]*1000%1000==0:
        cv2[i]=cv1[i]     
    else:
        cv2[i]=cv1[i]*1000        

#Medía y desviación de los cinco indicadores disponibles por municipio
medianvrm=np.round(nvrm2.mean(),1)
desviacionnvrm=np.round(nvrm2.std(),1)

mediaflr=np.round(cpflr2.mean(),1)
desviacionflr=np.round(cpflr2.std(),1)

mediamftrm=np.round(mftrm2.mean(),1)
desviacionmftrm=np.round(mftrm2.std(),1)

mediamlfr=np.round(mlfr2.mean(),1)
desviacionmlfr=np.round(mlfr2.std(),1)

mediacv=np.round(cv2.mean(),1)
desviacioncv=np.round(cv2.std(),1)

print('media de nacimientos',medianvrm,'desviacion de nacimientos',desviacionnvrm,sep='\t')
print('media de muertes fetales',mediamftrm,'desviacion de muertes fetales',desviacionmftrm,sep='\t')
print('media por matrimonio',mediamlfr,'desviacion por matrimonio',desviacionmlfr,sep='\t')
print('media de fallecidos',mediaflr,'desviacion de fallecidos',desviacionflr,sep='\t')
print('media de crecimiento',mediacv,'desviacion del crecimiento',desviacioncv,sep='\t')

#ahora que tenemos los valores enteros, podemos ordenar por fallecidos       
oflr=cpflr2[cpflr2[:,1].argsort()] 
oflr1=oflr.astype(str)
ln=len(oflr)
#para poder comparar los valores mayores a 1000:
for i in range(0,ln):
    if oflr[i,1]>999:
        palma=(oflr[i,1]/1000)
        palma1=str(palma)
        oflr1[i,1]=palma1 
        
oflr1[:,0]=np.char.rjust(oflr1[:,0],5,fillchar='0')
        
oflr2=np.full((ln,2),'valor',dtype='<U53')

for i in range(0,ln):
    for j in range (0,ln):
        if oflr1[i,0]==cpflr[j,0]:
            oflr2[i,0]=flr[j]
            oflr2[i,1]=oflr1[i,1]

print(oflr2)       