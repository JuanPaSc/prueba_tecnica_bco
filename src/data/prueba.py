import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("./src/data/books_data.csv")
df1 = pd.read_csv("./src/data/books_rating.csv")

# Mostrar las primeras filas del DataFrame
print(df1.head())
