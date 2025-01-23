import pandas as pd


class TopBooksAnalysis:
    def __init__(self, data: pd.DataFrame):
        """
        Constructor para inicializar el DataFrame de análisis.
        :param data: DataFrame que contiene los datos a analizar.
        """
        self.data = data

    def top_books_by_reviews(self, top_n=10):
        """
        Identifica los libros con mayor número de reseñas.
        :param top_n: Número de libros a devolver.
        :return: DataFrame con los libros más reseñados.
        """
        if "book_title" in self.data.columns:
            books_by_reviews = (
                self.data["book_title"].value_counts().head(top_n).reset_index()
            )
            books_by_reviews.columns = ["book_title", "review_count"]
            print(f"Top {top_n} libros por número de reseñas calculados.")
            return books_by_reviews
        else:
            print("Error: La columna 'book_title' no se encuentra en los datos.")
            return None

    def top_books_by_average_rating(self, top_n=10):
        """
        Identifica los libros mejor valorados por promedio de puntaje.
        :param top_n: Número de libros a devolver.
        :return: DataFrame con los libros mejor valorados por promedio de puntaje.
        """
        if "book_title" in self.data.columns and "rating" in self.data.columns:
            avg_rating = self.data.groupby("book_title")["rating"].mean().reset_index()
            avg_rating.rename(columns={"rating": "average_rating"}, inplace=True)
            top_books = avg_rating.sort_values(
                by="average_rating", ascending=False
            ).head(top_n)
            print(f"Top {top_n} libros por promedio de puntaje calculados.")
            return top_books
        else:
            print(
                "Error: Las columnas 'book_title' o 'rating' no se encuentran en los datos."
            )
            return None

    def top_books_by_sentiment(self, sentiment_data: pd.DataFrame, top_n=10):
        """
        Identifica los libros mejor valorados por promedio de sentimiento.
        :param sentiment_data: DataFrame que contiene las columnas 'book_title' y 'sentiment'.
        :param top_n: Número de libros a devolver.
        :return: DataFrame con los libros mejor valorados por promedio de sentimiento.
        """
        if (
            "book_title" in sentiment_data.columns
            and "sentiment" in sentiment_data.columns
        ):
            avg_sentiment = (
                sentiment_data.groupby("book_title")["sentiment"].mean().reset_index()
            )
            avg_sentiment.rename(
                columns={"sentiment": "average_sentiment"}, inplace=True
            )
            top_books = avg_sentiment.sort_values(
                by="average_sentiment", ascending=False
            ).head(top_n)
            print(f"Top {top_n} libros por promedio de sentimiento calculados.")
            return top_books
        else:
            print(
                "Error: Las columnas 'book_title' o 'sentiment' no se encuentran en los datos."
            )
            return None


# Ejemplo de uso
if __name__ == "__main__":
    # Simular carga de datos
    sample_data = {
        "book_title": ["Libro A", "Libro B", "Libro A", "Libro C", "Libro B"],
        "rating": [4, 5, 3, 4, 5],
    }
    sentiment_data = {
        "book_title": ["Libro A", "Libro B", "Libro A", "Libro C", "Libro B"],
        "sentiment": [0.8, 0.9, 0.7, 0.85, 0.9],
    }

    df = pd.DataFrame(sample_data)
    sentiment_df = pd.DataFrame(sentiment_data)

    # Crear instancia del análisis
    analysis = TopBooksAnalysis(df)

    # Libros más reseñados
    books_by_reviews = analysis.top_books_by_reviews()
    print(books_by_reviews)

    # Libros mejor valorados por puntaje
    books_by_rating = analysis.top_books_by_average_rating()
    print(books_by_rating)

    # Libros mejor valorados por sentimiento
    books_by_sentiment = analysis.top_books_by_sentiment(sentiment_df)
    print(books_by_sentiment)
