import pandas as pd


class ExploratoryAnalysis:
    def __init__(self, data: pd.DataFrame):
        """
        Constructor para inicializar el DataFrame de análisis.
        :param data: DataFrame que contiene los datos a analizar.
        """
        self.data = data

    def average_ratings_by_book(self):
        """
        Calcula el promedio de valoraciones por libro.
        :return: DataFrame con libros y sus valoraciones promedio.
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
        :return: Diccionario con el número total de reseñas y valoraciones.
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
        :param top_n: Número de autores populares a devolver.
        :return: DataFrame con los autores más populares.
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
        :param top_n: Número de categorías populares a devolver.
        :return: DataFrame con las categorías más reseñadas.
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


# # Ejemplo de uso
# if __name__ == "__main__":
#     # Simular carga de datos
#     sample_data = {
#         'book_title': ['Libro A', 'Libro B', 'Libro A', 'Libro C', 'Libro B'],
#         'rating': [4, 5, 3, 4, 5],
#         'author': ['Autor X', 'Autor Y', 'Autor X', 'Autor Z', 'Autor Y'],
#         'category': ['Ficción', 'Ficción', 'Ficción', 'Ciencia', 'Ficción']
#     }
#     df = pd.DataFrame(sample_data)

#     # Crear instancia del análisis
#     analysis = ExploratoryAnalysis(df)

#     # Calcular valoraciones promedio
#     avg_ratings = analysis.average_ratings_by_book()
#     print(avg_ratings)

#     # Total de reseñas y valoraciones
#     totals = analysis.total_reviews_and_ratings()
#     print(totals)

#     # Autores más populares
#     popular_authors = analysis.most_popular_authors()
#     print(popular_authors)

#     # Categorías más reseñadas
#     popular_categories = analysis.most_reviewed_categories()
#     print(popular_categories)
