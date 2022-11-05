# Importamos pandas, leemos el csv y creamos el dataframe a utilizar

import pandas as pd

df = pd.read_csv("csv\\netflix.csv")


# Cambiamos el tipo de dato de date_added(object) a datetime

df.date_added = pd.to_datetime(df.date_added)


# Ordenamos el df por fecha

df.sort_values(by=['date_added'], inplace=True)


# Reemplazamos los Not Given en director por None

df.director.replace('Not Given', None, inplace=True)

# Creamos 3 dataframes a partir de la fecha de lanzamiento de la pelicula

mask1 = (df.release_year == 2019)
mask2 = (df.release_year == 2020)
mask3 = (df.release_year == 2021)

df2019 = df[mask1]
df2020 = df[mask2]
df2021 = df[mask3]

# Creamos 3 diccionarios a partir de los dataframes anteriores

dict_2019 = df2019.reset_index().to_dict(orient="index")
dict_2020 = df2020.reset_index().to_dict(orient="index")
dict_2021 = df2021.reset_index().to_dict(orient="index")