#Importamos las librerias 
import pandas as pd
import numpy as np
# array de 5 numeros aleatorios
arr = np.random.randint(1,10 , size=5)
print(f'Array de numeros aleatorios: {arr}')

#Creamos el df del  arr y nombramos la columna 'numeros'
df_numeros = pd.DataFrame(arr , columns= ['Numeros'])

#Multiplicamos x2 para generar los dobles
df_numeros['Dobles'] = df_numeros['Numeros']*2

print(df_numeros)