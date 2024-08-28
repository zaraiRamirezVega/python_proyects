import pandas as pd

data = {
    'Nombre' : ['Juan' , 'Ana' , 'Luis', 'Marta'],
    'Edad' : [15 , 14 , 16 , 15],
    'Nota' : [8.5 , 9.0 , 7.5 , 8.0]
}

#Creamos el dataframe de la data
df = pd.DataFrame(data)


#Agregamos una nueva columna
ciudades = ['Madrid' , 'Barcelona' , 'Valencia', 'Sevilla']
df['Ciudad'] = ciudades
#Mostramos el dataframe actualizado
print('DataFrame actualizado: \n')
print(df)