import pandas as pd


class TopBooksAnalysis:
    """
    Clase para realizar análisis de libros top en base a reseñas, valoraciones y sentimientos.

    Attributes:
        data (pd.DataFrame): DataFrame que contiene los datos de análisis.
    """
    def __init__(self, data: pd.DataFrame):
        """
        Constructor para inicializar el DataFrame de análisis.

        Args:
            data (pd.DataFrame): DataFrame que contiene los datos a analizar.
        """
        self.data = data

    def top_books_by_reviews(self, top_n=10):
        """
        Identifica los libros con mayor número de reseñas.

        Args:
            top_n (int): Número de libros a devolver. Por defecto, 10.

        Returns:
            pd.DataFrame: DataFrame con los títulos de los libros y el número de reseñas.
                          Contiene dos columnas: 'book_title' y 'review_count'.
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

        Args:
            top_n (int): Número de libros a devolver. Por defecto, 10.

        Returns:
            pd.DataFrame: DataFrame con los títulos de los libros y su promedio de puntaje.
                          Contiene dos columnas: 'book_title' y 'average_rating'.
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

        Args:
            sentiment_data (pd.DataFrame): DataFrame que contiene las columnas 'book_title' y 'sentiment'.
            top_n (int): Número de libros a devolver. Por defecto, 10.

        Returns:
            pd.DataFrame: DataFrame con los títulos de los libros y su promedio de sentimiento.
                          Contiene dos columnas: 'book_title' y 'average_sentiment'.
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

