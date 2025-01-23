from src.modules.analisis_exp import ExploratoryAnalysis
from src.modules.analisis_NLP import SentimentAnalysis
from src.modules.cargar_data import cargar_data
from src.modules.top_libros import TopBooksAnalysis
from src.modules.visualizacion import DataVisualization

def main():
    # Ruta de los datos
    book_details_path = "./src/data/books_data.csv"
    reviews_path = "./src/data/books_rating.csv"

    # === Módulo de Carga de Datos ===
    print("Cargando datos...")
    book_loader = cargar_data(book_details_path)
    books_data = book_loader.load_csv()
    books_data = book_loader.clean_csv()

    reviews_loader = cargar_data(reviews_path)
    reviews_data = reviews_loader.load_csv()
    reviews_data = reviews_loader.clean_csv()

    # Detectar anomalías
    print("\nDetectando anomalías en los datos de valoraciones...")
    anomalies_books = book_loader.detect_outliers("ratingsCount")
    anomalies_reviews = reviews_loader.detect_outliers("review/score")

    # === Módulo de Análisis de Sentimientos ===
    print("\nRealizando análisis de sentimientos...")
    sentiment_analyzer = SentimentAnalysis()
    reviews_data["sentiment"] = sentiment_analyzer.analyze_sentiments(reviews_data["review/text"])

    # === Módulo de Análisis ===
    print("\nGenerando métricas y estadísticas...")
    data_analyzer = ExploratoryAnalysis(books_data, reviews_data)
    top_books_by_reviews = data_analyzer.top_books_by_reviews(10)
    top_books_by_rating = data_analyzer.top_books_by_rating(10)
    top_books_by_sentiment = data_analyzer.top_books_by_sentiment(10)

    # === Módulo de Visualización ===
    print("\nGenerando visualizaciones...")
    visualizer = DataVisualization()
    visualizer.plot_top_books(top_books_by_reviews, title="Top 10 libros por número de reseñas")
    visualizer.plot_top_books(top_books_by_rating, title="Top 10 libros por puntaje promedio")
    visualizer.plot_top_books(top_books_by_sentiment, title="Top 10 libros por sentimiento promedio")

    # Mostrar resultados finales
    print("\nResultados:")
    print("Top 10 libros por número de reseñas:")
    print(top_books_by_reviews)
    print("\nTop 10 libros por puntaje promedio:")
    print(top_books_by_rating)
    print("\nTop 10 libros por sentimiento promedio:")
    print(top_books_by_sentiment)

if __name__ == "__main__":
    main()
