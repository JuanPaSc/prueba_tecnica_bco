import pandas as pd


class cargar_data:
    """
    Modulo diseñado para cargar los archivos csv 
    que contienen la información de los libros y 
    reseñas de los mismos por id de reseña.
    """

    def __init__(self, file_path: str):
        """ """
        self.file_path = file_path
        self.data = None

    def load_csv(self):
        """
        Carga un archivo CSV desde la ruta especificada y lo almacena 
        en el atributo `self.data`. Tratará de cargar el archivo, e 
        informará de un error si no se encuentra o si ocurre algún 
        problema durante la carga.
        ---------------------------------------------------------------
        Returns:
            pd.DataFrame: Un DataFrame con los datos cargados del archivo CSV. 
            Si ocurre un error, devuelve None.
        """
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Archivo CSV cargado desde {self.file_path}")
        except FileNotFoundError:
            print(f"Error: El archivo csv no fue encontrado en {self.file_path}")
        except Exception as e:
            print(f"Error: No se cargó el archivo CSV {e}")
        return self.data

    def clean_csv(self):
        """
        Limpia los datos cargados eliminando valores nulos y duplicados.

        Operaciones realizadas:
            - Verifica y muestra los valores nulos por columna.
            - Elimina las filas con valores nulos.
            - Elimina filas duplicadas.
        ---------------------------------------------------------------
        Returns:
            pd.DataFrame: Un DataFrame limpio. 
            Si no se han cargado datos, devuelve None.
        """
        if self.data is not None:
            null_values = self.data.isnull().sum()
            print(f"Valores nulos por columna: \n", null_values)

            self.data.dropna(inplace=True)
            print("Datos limpiados: Valores nulos")
            self.data.drop_duplicates(inplace=True)
            print("Datos limpiados: Valores duplicados")
        else:
            print(f"Error: Los datos del archivo CSV no fueron cargados en load_csv()")
        return self.data

    def detect_outliers(self, column: str):
        """
        Detecta valores atípicos (outliers) en una columna 
        específica usando el método del rango intercuartil (IQR).
        ---------------------------------------------------------------
        Args:
            column (str): El nombre de la columna en la que se buscarán outliers.
        ---------------------------------------------------------------
        Returns:
            pd.DataFrame: Un DataFrame con las filas que contienen valores atípicos. 
            Si la columna no existe o los datos no están cargados, devuelve None.
        ---------------------------------------------------------------
        Raises:
            ValueError: Si la columna especificada no está en los datos.
        """
        if self.data is not None and column in self.data.columns:
            q1 = self.data[column].quantile(0.25)
            q3 = self.data[column].quantile(0.75)
            iqr = q3 - q1

            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            anomalies = self.data[(self.data[column] < lower_bound) | (self.data[column] > upper_bound)]
            print(f"Se detectaron {len(anomalies)} anomalías en la columna '{column}'.")
            return anomalies
        else:
            print(f"Error: Columna '{column}' no encontrada o datos no cargados.")
            return None
