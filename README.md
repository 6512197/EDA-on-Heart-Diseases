# Análisis Exploratorio de Datos (EDA) sobre enfermedades cardíacas

![Cabecera](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.JaaC1fPXkZubAc5nmOdkhQHaGB%26pid%3DApi&f=1&ipt=8aa4f55c9ca2f0e547428837fecc4750617f1f8d166a11770be62eb13c7a3c82&ipo=images)

El presente EDA se centra en el estudio de dos conjuntos de datos valiosos para la investigación médica. El primero proviene de un hospital multispecializado y contiene información detallada sobre 1000 sujetos con 14 características comunes, siendo fundamental para la detección temprana y modelos predictivos de enfermedades cardíacas mediante el aprendizaje automático. El segundo conjunto, obtenido de Kaggle, se enfoca en predecir accidentes cerebrovasculares, usando parámetros como edad, género y estado de fumador. Ha sido filtrado para su uso en aprendizaje automático y visualización de datos, proporcionando detalles sobre individuos, incluyendo la ocurrencia de accidentes cerebrovasculares y otros detalles médicos.

## Objetivos del EDA 
- Analizar la estructura, distribución y tipos de datos presentes en el conjunto de datos.
- Identificar correlaciones, relaciones y patrones dentro de los datos para comprender mejor las interacciones entre las variables.
- Realizar limpieza de datos, como manejar valores faltantes, transformar variables y normalizar datos para facilitar análisis adicionales.
- Crear gráficos y visualizaciones que comuniquen de manera efectiva la información contenida en los datos.
- Ofrecer información útil para la toma de decisiones informadas en investigaciones científicas.

## Hipótesis
1) Relación entre género y enfermedades cardíacas: se presume que los hombres tienen una mayor incidencia de enfermedades cardíacas en comparación con las mujeres.
2) Impacto de los factores de riesgo en enfermedades cardíacas: se busca analizar la correlación entre la edad y el nivel de glucosa con la presencia de enfermedades cardíacas o accidentes cerebrovasculares.
3) Tipo de trabajo, estilo de vida y problemas cardiovasculares: se investigará si ciertos tipos de trabajo, niveles de actividad física o entornos urbanos se relacionan con diferentes tasas de enfermedades cardíacas.
4) Relación entre el nivel de glucosa y la diabetes: se explorará si niveles más altos de glucosa están asociados con una mayor probabilidad de desarrollar diabetes, la cual a su vez puede estar vinculada con problemas cardíacos.

## Contenido
Este análisis se basa en datos públicos provenientes de fuentes confiables como [EU Data](https://data.europa.eu/) y artículos de investigación de [WHO](https://www.who.int/). Se divide en cuatro secciones principales:

1) Introducción y contexto.
2) Descripción de los datos.
3) Análisis del primer y segundo dataframe.
4) Modificación de datos.
5) Hipótesis.

***
## Apéndices

### Futuras líneas de estudio
Se abren múltiples posibilidades para investigaciones futuras a partir de este EDA. Algunas ideas incluyen:
* ¿Existe una relación significativa entre el estado civil y el nivel de estrés percibido en diferentes grupos de edad?
* Acceso a la atención médica: Diferencias en el acceso a servicios de salud entre hombres y mujeres debido a barreras sociales, económicas o culturales.

## Fuentes (referencias utilizadas para aumentar la comprensión del tema)
* JACC Journals: [Enlace](https://www.jacc.org/doi/10.1016/j.jacc.2023.11.007)
* WHO: [Enlace](https://www.who.int/europe/news/item)
* EU Data: [Enlace](https://data.europa.eu/es)
* Kaggle: [Enlace](https://www.kaggle.com/datasets)

### Requerimientos
    - numpy==1.21.6
    - packaging==23.1
    - pandas==1.3.5
    - plotly==5.14.1
    - python==3.10.0

### Autora
Aya Dahmani [GitHub](https://github.com/6512197)
