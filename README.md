# prueba_tecnica_bco
Repositorio creado con la única finalidad de desarrollar la prueba técnica de ciencia de datos para la vacante de Analítico Sección Logística

# README

## Proyecto: Análisis y Visualización de Libros y Reseñas

Este proyecto se centra en el análisis de un conjunto de datos de libros y reseñas de Amazon mediante técnicas de procesamiento de lenguaje natural (NLP) y análisis exploratorio de datos. El código está estructurado de manera modular, utilizando principios de buenas prácticas de desarrollo.

---

## Estructura del Proyecto

El proyecto está dividido en los siguientes módulos:

1. **Carga y Limpieza de Datos (`cargar_data.py`)**
   - Clase `cargar_data`: Permite cargar datos desde archivos CSV, limpiar valores nulos y duplicados, y detectar valores atípicos (outliers) en columnas específicas.

2. **Análisis Exploratorio (`analisis_exp.py`)**
   - Clase `ExploratoryAnalysis`: Incluye métodos para calcular promedios de valoraciones, contar reseñas y valoraciones totales, y determinar los autores y categorías más populares.

3. **Análisis de Sentimientos (`analisis_NLP.py`)**
   - Clase `SentimentAnalysis`: Proporciona herramientas para preprocesar textos de reseñas, calcular puntajes de sentimientos usando TextBlob y agrupar el promedio de sentimientos por libros o categorías.

4. **Análisis de Libros Principales (`top_libros.py`)**
   - Clase `TopBooksAnalysis`: Identifica los libros más reseñados, mejor valorados por promedio de puntuación y por sentimientos.

5. **Visualización de Datos (`visualizacion.py`)**
   - Clase `DataVisualization`: Genera gráficos utilizando Matplotlib y Seaborn para mostrar los libros más reseñados, autores más populares, distribución de sentimientos y más.

6. **Archivo Principal (`main.py`)**
   - Integra todas las funcionalidades de los módulos anteriores y permite la ejecución completa del flujo de análisis.

---

Requisitos Previos

1. Crear un Ambiente Virtual

Se recomienda crear un entorno virtual para gestionar las dependencias. Siga los siguientes pasos:

python -m venv .venv
source .venv/bin/activate  # En Linux/MacOS
.venv\Scripts\activate    # En Windows

2. Instalar Dependencias

Las dependencias necesarias están especificadas en el archivo requirements.txt. Para instalarlas, ejecute:

pip install -r requirements.txt

3. Ubicación de los Datos

Los archivos CSV descargados desde Kaggle deben colocarse en la siguiente ubicación:

src/data/

El archivo de detalles de libros debe llamarse book_details.csv y el de reseñas reviews.csv.
---

## Ejecución del Proyecto

El archivo principal `main.py` consolida todas las funcionalidades. Para ejecutarlo:

```bash
python main.py
```

Este archivo realiza las siguientes acciones:

1. Carga los datos de libros y reseñas.
2. Limpia los datos y verifica la existencia de valores nulos y duplicados.
3. Realiza un análisis exploratorio de datos, incluyendo:
   - Promedio de valoraciones por libro.
   - Autores y categorías más populares.
4. Aplica análisis de sentimientos a las reseñas.
5. Identifica los libros más destacados por reseñas, puntuación promedio y sentimiento.
6. Genera visualizaciones clave para el análisis de resultados.

---

## Ejemplo de Uso

### Datos de Ejemplo
Los datos utilizados en los módulos son simulados para propósitos de demostración. El conjunto de datos real debe descargarse desde [este enlace](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews).

### Salida del Proyecto
- DataFrames procesados con información clave.
- Gráficos para interpretar visualmente los resultados.

---

## Estructura del Repositorio

```
├── src
    ├──── modules
        ├──── cargar.py
        ├──── exploratory_analysis.py
        ├──── sentiment_analysis.py
        ├──── top_books_analysis.py
        ├──── data_visualization.py
    ├──── data
        ├──── books_data.csv
        ├──── books_rating.csv
    ├──── static
        ├──── config.json         
├── main.py
├── README.md
├── report.md
└── requirements.txt
```

---