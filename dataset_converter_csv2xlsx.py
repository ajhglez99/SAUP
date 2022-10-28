import pandas as pd

df = pd.read_excel("./datasets/database.xlsx")

del df['Fecha de publicación']
del df['Polaridad en Inglés']
del df['Polaridad en Español']
del df['Clase con Inglés']
del df['Clase con Español']
del df['Clase']

df.to_csv("./datasets/database.csv", sep=",", index = False)