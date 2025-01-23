import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class DataVisualization:
    """
    Clase para generar visualizaciones basadas en los datos de libros y reseñas.

    Attributes:
        book_details (pd.DataFrame): DataFrame con detalles de los libros, como autores y categorías.
        reviews (pd.DataFrame): DataFrame con información de las reseñas, como puntuaciones y sentimientos.
    """
    def __init__(self, book_details: pd.DataFrame, reviews: pd.DataFrame):
        """
        Inicializa el módulo de visualización con los datos necesarios.

        Args:
            book_details (pd.DataFrame): DataFrame que contiene detalles de los libros.
            reviews (pd.DataFrame): DataFrame que contiene información de las reseñas.
        """
        self.book_details = book_details
        self.reviews = reviews

    def plot_top_books_by_reviews(self, top_n=10):
        """
        Genera un gráfico de barras con los libros más reseñados.

        Args:
            top_n (int): Número de libros a mostrar. Por defecto, 10.
        """
        review_counts = self.reviews['book_title'].value_counts().head(top_n)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=review_counts.values, y=review_counts.index, palette="viridis")
        plt.title(f"Top {top_n} Libros con Más Reseñas", fontsize=16)
        plt.xlabel("Número de Reseñas", fontsize=12)
        plt.ylabel("Título del Libro", fontsize=12)
        plt.show()

    def plot_top_authors_by_books(self, top_n=10):
        """
        Genera un gráfico de barras con los autores más populares por cantidad de libros.

        Args:
            top_n (int): Número de autores a mostrar. Por defecto, 10.
        """
        author_counts = self.book_details['authors'].value_counts().head(top_n)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=author_counts.values, y=author_counts.index, palette="magma")
        plt.title(f"Top {top_n} Autores con Más Libros", fontsize=16)
        plt.xlabel("Número de Libros", fontsize=12)
        plt.ylabel("Autor", fontsize=12)
        plt.show()

    def plot_average_ratings_by_category(self, top_n=10):
        """
        Genera un gráfico de barras con las categorías mejor valoradas en promedio.

        Args:
            top_n (int): Número de categorías a mostrar. Por defecto, 10.
        """
        category_ratings = self.book_details.groupby('categories')['average_rating'].mean().sort_values(ascending=False).head(top_n)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=category_ratings.values, y=category_ratings.index, palette="coolwarm")
        plt.title(f"Top {top_n} Categorías Mejor Valoradas", fontsize=16)
        plt.xlabel("Promedio de Valoración", fontsize=12)
        plt.ylabel("Categoría", fontsize=12)
        plt.show()

    def plot_sentiment_distribution(self):
        """
        Genera un histograma de la distribución de sentimientos en las reseñas.
        """
        if 'sentiment_score' not in self.reviews.columns:
            raise ValueError("La columna 'sentiment_score' no está en el DataFrame de reseñas.")
        plt.figure(figsize=(10, 6))
        sns.histplot(self.reviews['sentiment_score'], bins=20, kde=True, color="skyblue")
        plt.title("Distribución de Sentimientos en Reseñas", fontsize=16)
        plt.xlabel("Puntaje de Sentimiento", fontsize=12)
        plt.ylabel("Frecuencia", fontsize=12)
        plt.show()
