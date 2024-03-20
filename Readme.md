![Cabecero](.[image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.JaaC1fPXkZubAc5nmOdkhQHaGB%26pid%3DApi&f=1&ipt=8aa4f55c9ca2f0e547428837fecc4750617f1f8d166a11770be62eb13c7a3c82&ipo=images))


# Análisis Exploratorio de Datos (EDA) sobre enfermedades cardíacas

El presente EDA trata sobre un estudio de dos conjuntos "Estos conjuntos de datos son valiosos recursos para la investigación médica. El primero aborda enfermedades cardíacas y se obtuvo de un hospital multispecializado. Contiene una amplia gama de información sobre 1000 sujetos, con 14 características comunes y se considera fundamental para la detección temprana y modelos predictivos de enfermedades cardíacas mediante el aprendizaje automático. El segundo conjunto de datos, proveniente de Kaggle, se centra en predecir accidentes cerebrovasculares utilizando parámetros como edad, género y estado de fumador. Se ha filtrado para el aprendizaje automático y la visualización de datos, ofreciendo detalles sobre individuos, incluyendo la ocurrencia de accidentes cerebrovasculares y otros detalles médicos, donde 'Unknown' indica datos no disponibles y 'N/A' indica información no aplicable.

## Objetivos del EDA 
- Analizar la estructura, distribución y tipos de datos presentes en el conjunto de datos.
- Buscar correlaciones, relaciones y patrones dentro de los datos para comprender mejor las interacciones entre las variables.
- Realizar limpieza de datos, como manejar valores faltantes, transformar variables y normalizar datos para facilitar análisis adicionales.
- Crear gráficos y visualizaciones que comuniquen de manera efectiva la información contenida en los datos.
- Proporcionar información que pueda ser útil para tomar decisiones informadas en investigaciones científicas.




## Hipótesis
1) Relación entre género y enfermedades cardíacas: los hombres tienden a tener una mayor incidencia de enfermedades cardíacas en comparación con las mujeres.
2) Impacto de los factores de riesgo en enfermedades cardíacas: la edad y el nivel de glucosa podrían estar correlacionadas con la presencia de enfermedades cardíacas o accidentes cerebrovasculares. 
3) Tipo de trabajo, estilo de vida y problemas cardiovasculares: las personas con ciertos tipos de trabajo, niveles de actividad física o entornos urbanos tienen diferentes tasas de enfermedades cardíacas.
4) Relación entre el nivel de glucosa y la diabetes: niveles más altos de glucosa están asociados con una mayor probabilidad de desarrollar diabetes, que a su vez puede estar vinculada con problemas cardíacos...


## Contenido
Este análisis ha sido realizado utilizando datos públicos de fuentes confiables como el  [EU Data](https://data.europa.eu/) o artículos de investigación de [WHO](https://www.who.int/ ). El análisis se divide en cuatro secciones principales:

1) Introducción y contexto:
El presente análisis tiene como objetivo examinar dos conjuntos de datos diferentes para identificar posibles correlaciones entre la edad y el nivel de estrés en una muestra de población. Se busca entender la relación entre estos factores y evaluar si existe una posible asociación.
2) Descripción de los datos.
3) Análisis del primer y el segundo dataframe.
4) Modificación de datos.
5) Hypothesis.


***
## Apéndices

### Futuras líneas de estudio
El estudio de este EDA permite que se abra una miríada de posibilidades para investigaciones futuras. creemos que se puede continuar la investigación en torno a cuestiones como:
* ¿Existe una relación significativa entre el estado civil y el nivel de estrés percibido, considerando diferentes grupos de edad?
* Acceso a la atención médica: Puede haber diferencias en el acceso a la atención médica entre hombres y mujeres. Por ejemplo, en algunas culturas o regiones, las mujeres pueden tener menos acceso a los servicios de salud debido a barreras sociales, económicas o culturales...

## Fuentes (some refences i used in order to help increase my understanding of the topic )
*  jacc journals [https://www.jacc.org/doi/10.1016/j.jacc.2023.11.007]
* who [https://www.who.int/europe/news/item]
* data eu [https://data.europa.eu/es]
* kaggle [https://www.kaggle.com/datasets]
***
### Requirements
    numpy==1.21.6
    packaging==23.1
    pandas==1.3.5
    plotly==5.14.1
    python==3.10.0
***
### Autora
Aya Dahmani [https://github.com/6512197](https://github.com/6512197)