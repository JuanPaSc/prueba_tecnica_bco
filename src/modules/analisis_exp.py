import pandas as pd


class ExploratoryAnalysis:
    """
    Clase para realizar análisis exploratorio en un conjunto de datos de libros y reseñas.

    Attributes:
        data (pd.DataFrame): DataFrame que contiene los datos a analizar.
    """
    def __init__(self, data: pd.DataFrame):
        """
        Constructor para inicializar el DataFrame de análisis.

        Args:
            data (pd.DataFrame): DataFrame que contiene los datos a analizar.
        """
        self.data = data

    def average_ratings_by_book(self):
        """
        Calcula el promedio de valoraciones por libro.

        Agrupa los datos por título del libro y calcula el promedio de las valoraciones.

        Returns:
            pd.DataFrame: DataFrame con las columnas `book_title` y `average_rating`.
            Devuelve None si faltan las columnas necesarias.
        """
        if "book_title" in self.data.columns and "rating" in self.data.columns:
            avg_ratings = self.data.groupby("book_title")["rating"].mean().reset_index()
            avg_ratings.rename(columns={"rating": "average_rating"}, inplace=True)
            print("Valoraciones promedio calculadas por libro.")
            return avg_ratings
        else:
            print(
                "Error: Las columnas 'book_title' o 'rating' no se encuentran en los datos."
            )
            return None

    def total_reviews_and_ratings(self):
        """
        Determina el número total de reseñas y valoraciones en el DataFrame.

        Returns:
            dict: Diccionario con el total de reseñas (`total_reviews`) 
            y el total de valoraciones (`total_ratings`).
        """
        total_reviews = self.data.shape[0]
        total_ratings = (
            self.data["rating"].count() if "rating" in self.data.columns else 0
        )
        print(
            f"Total de reseñas: {total_reviews}, Total de valoraciones: {total_ratings}."
        )
        return {"total_reviews": total_reviews, "total_ratings": total_ratings}

    def most_popular_authors(self, top_n=10):
        """
        Identifica los autores más populares basándose en la cantidad de libros o reseñas.

        Args:
            top_n (int, optional): Número de autores más populares a devolver. 
                                   Por defecto es 10.

        Returns:
            pd.DataFrame: DataFrame con las columnas `author` y `count`, 
                          ordenado por popularidad. Devuelve None si falta la columna `author`.
        """
        if "author" in self.data.columns:
            popular_authors = (
                self.data["author"].value_counts().head(top_n).reset_index()
            )
            popular_authors.columns = ["author", "count"]
            print(f"Top {top_n} autores más populares calculados.")
            return popular_authors
        else:
            print("Error: La columna 'author' no se encuentra en los datos.")
            return None

    def most_reviewed_categories(self, top_n=10):
        """
        Identifica los géneros o categorías más reseñados.

        Args:
            top_n (int, optional): Número de categorías populares a devolver. 
                                   Por defecto es 10.

        Returns:
            pd.DataFrame: DataFrame con las columnas `category` y `count`, 
                          ordenado por popularidad. Devuelve None si falta la columna `category`.
        """
        if "category" in self.data.columns:
            popular_categories = (
                self.data["category"].value_counts().head(top_n).reset_index()
            )
            popular_categories.columns = ["category", "count"]
            print(f"Top {top_n} géneros/categorías más reseñadas calculadas.")
            return popular_categories
        else:
            print("Error: La columna 'category' no se encuentra en los datos.")
            return None
