import pandas as pd


class cargar_data:
    """ """

    def __init__(self, file_path: str):
        """ """
        self.file_path = file_path
        self.data = None

    def load_csv(self):
        """ """
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Archivo CSV cargado desde {self.file_path}")
        except FileNotFoundError:
            print(f"Error: El archivo csv no fue encontrado en {self.file_path}")
        except Exception as e:
            print(f"Error: No se cargó el archivo CSV {e}")
        return self.data

    def clean_csv(self):
        """ """
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
        """ """
        pass
