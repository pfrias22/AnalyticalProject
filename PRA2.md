# PRÁCTICA 2 - LIMPIEZA Y VALIDACIÓN DE LOS DATOS

## DESCRIPCIÓN DEL DATASET

El conjunto de datos seleccionado para el análisis se ha conseguido en [Kaggle](https://www.kaggle.com/c/titanic). El dataset obtenido contiene registros sobre los pasajeros que abordaron el transatlántico Titanic el 10 de abril de 1912 desde el puerto Southampton y los pasajeros que se incorporaron en los puertos de Cherburgo, Francia, y en Queenstown en Irlanda.

Este conjunto de datos de entrenamiento está compuesto por 12 atributos que representan 891 pasajeros que navegaban en el titanic.

Los campos de este conjunto de datos son los siguientes:

- PassengerId
- Survived: indica si el pasajero ha sobrevivido o no.
- Pclass: clase en la que viajaba el pasajero.
- Name: nombre del pasajero.
- Sex: sexo del pasajero.
- Age: edad del pasajero.
- SibSp: número de hermano/conyuge a bordo.
- Parch: número de padres/hijos a bordo.
- Ticket: tipo de ticket del pasajero.
- Fare: tarifa correspondiente al ticker del pasajero.
- Cabin: la cabina donde se hospeda el pasajero.
- Embarked: el puerto donde los pasajeros han embarcado.

### Importancia y objetivos de los análisis

Con este conjunto de datos se plantea la problemática de determinar qué variables influyen más sobre supervivencia de un pasajero en el Titanic. Además, se podrá proceder a crear modelos de regresión que permitan predecir la supervivencia de un pasajero en función de sus características y contrastes de hipótesis que ayuden a identificar propiedades interesantes en las muestras que puedan ser inferidas con respecto a la población.

Estos análisis adquieren una gran relevancia en casi cualquier sector relacionado con la navegación. Un ejemplo de ello...

## INTEGRACIÓN Y SELECCIÓN DE LOS DATOS DE INTERÉS A ANALIZAR

Antes de comenzar con la limpieza de los datos, procedemos a realizar la lectura del fichero en formato CSV en el que se encuentran. El resultado devuelto por la llamada a la función read.csv() será un objeto data.frame:

![Lectura de datos](./images/read.png)

Además, observamos cómo los tipos de datos asignados automáticamente por Python a las variables
se corresponden con el dominio de estas.

La gran mayoría de los atributos del conjunto de datos pertenecen a características que poseen los diferentes pasajeros contenidos en el dataset, por lo que
será conveniente tenerlos en cuenta durante la realización del proceso de análisis

Sin embargo, podemos prescindir del primer campo (`PassengerId`) dado que no son atributos propios de los pasajeros y, por tanto, resulta menos relevante a la
hora de resolver nuestro problema.

![Gestión de atributos](./images/atributos.png)

## LIMPIEZA DE LOS DATOS

### ¿Los datos contienen ceros o elementos vacíos?

![Lectura de nulos](./images/nulos.png)

### ¿Cómo gestionarías cada uno de estos casos?

Existen diferentes maneras de gestionar los elementos vacíos:

- Reemplazar el elemento vacío por un valor (constante, media, mediana...).
- Eliminar las filas con elementos vacíos.

En nuestro caso, reemplazaremos el elemento vacío por un valor:

- Para el atributo `Age`, reemplazaremos los elementos vacíos por la media.
- Constante en el caso del atributo `Cabin` que será una cadena vacía (" ").
- Para el atributo `Embarked`, reemplazaremos los valores vacíos por una cadena vacía (" ").

![Gestión de nulos](./images/replace.png)

### Identificación y tratamiento de valores extremos

Los valores extremos o outliers son aquellos que parecen no ser coherentes si realizamos una comparación con el resto de los datos. Para identificarlos, podemos hacer uso de dos vías:

- Representar un diagrama de caja por cada variable y ver qué valores distan mucho del rango intercuartílico (la caja).
- Utilizar la función boxplots.stats() de R, la cual se emplea a continuación.

Así, se mostrarán sólo los valores atípicos para aquellas variables que los contienen:

![Atípicos](./images/atipicos.png)

Función para eliminar valores atítipicos:

![Atípicos](./images/outliers.png)

## ANÁLISIS DE LOS DATOS

### Selección de los grupos de datos que se quieren analizar/comparar (planificación de los análisis a aplicar).

A continuación, se seleccionan los grupos dentro de nuestro conjunto de datos que pueden resultar interesantes para analizar y/o comparar.

![Selección grupos](./images/agrupacion.png)

### Comprobación de la normalidad y homogeneidad de la varianza

Para realizar la comprobación de que los valores que toman nuestras variables cuantitativas provienen de una población distribuida normalmente, utilizaremos la prueba de normalidad de Shapiro-Wilk.
Así, se comprueba que para que cada prueba se obtiene un p-valor superior al nivel de significación prefijado alfa = 0, 05. Si esto se cumple, entonces se considera que variable en cuestión sigue una distribución normal.

### Aplicación de pruebas estadísticas para comparar los grupos de datos. En función de los datos y el objetivo del estudio, aplicar pruebas de contraste de hipótesis, correlaciones, regresiones, etc. Aplicar al menos tres métodos de análisis diferentes

## Representación de los resultados a partir de tablas y gráficas

## Resolución del problema. A partir de los resultados obtenidos, ¿cuáles son las conclusiones? ¿Los resultados permiten responder al problema?

## CONTRIBUCIONES AL TRABAJO

| Contribuciones  | Firma  |
|---|---|
| Investigación previa  | PFA,   |
| Redacción de las respuestas  | PFA,   |
| Desarrollo código | PFA,  |
