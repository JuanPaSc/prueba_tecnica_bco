import pandas as pd
from textblob import TextBlob
import re
import string


class SentimentAnalysis:
    def __init__(self, dataframe: pd.DataFrame, text_column: str = "review/text"):
        """
        Inicializa el módulo con el DataFrame y la columna de texto.
        :param dataframe: DataFrame que contiene las reseñas.
        :param text_column: Nombre de la columna con el texto de las reseñas.
        """
        self.dataframe = dataframe
        self.text_column = text_column
        self.sentiment_column = "sentiment_score"

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Limpia el texto eliminando puntuación, convirtiendo a minúsculas y eliminando caracteres especiales.
        :param text: Cadena de texto original.
        :return: Texto limpio.
        """
        text = text.lower()
        # Convertiendo reseña a minúsculas
        text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
        # "Eliminando los signos de puntuación de la reseña
        text = re.sub(r"\s+", " ", text).strip()
        # Eliminando espacios extras al inicio y final de la reseña
        return text

    def preprocess_reviews(self):
        """
        Preprocesa la columna de texto, aplicando limpieza.
        """
        if self.text_column not in self.dataframe.columns:
            raise ValueError(
                f"La columna '{self.text_column}' no existe en el DataFrame."
            )
        self.dataframe[self.text_column] = (
            self.dataframe[self.text_column].astype(str).apply(self.clean_text)
        )

    @staticmethod
    def analyze_sentiment(text: str) -> float:
        """
        Aplica un análisis de sentimiento utilizando TextBlob.
        :param text: Texto a analizar.
        :return: Puntaje de sentimiento (positivo: > 0, negativo: < 0, neutral: 0).
        """
        blob = TextBlob(text)
        return blob.sentiment.polarity

    def calculate_sentiments(self):
        """
        Calcula el sentimiento para cada reseña en el DataFrame.
        """
        self.dataframe[self.sentiment_column] = self.dataframe[self.text_column].apply(
            self.analyze_sentiment
        )

    def average_sentiment_by(self, group_column: str) -> pd.DataFrame:
        """
        Calcula el promedio del sentimiento agrupado por una columna específica (ej. libro o categoría).
        :param group_column: Nombre de la columna por la cual agrupar (ej. "book_title" o "category").
        :return: DataFrame con el promedio de sentimiento por grupo.
        """
        if group_column not in self.dataframe.columns:
            raise ValueError(f"La columna '{group_column}' no existe en el DataFrame.")
        return (
            self.dataframe.groupby(group_column)[self.sentiment_column]
            .mean()
            .reset_index()
            .rename(columns={self.sentiment_column: "average_sentiment"})
        )
