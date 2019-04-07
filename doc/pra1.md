
# PRA 1

### Contexto

Los datos han sido extraídos de la página oficial de la [FIFA](https://www.fifa.com) (Federación Internacional de Fútbol Asociado). Tratándose de información sobre el mundial de futbol celebrado en Rusia en 2018 he considerado que la información suministrada por los propios organizadores del evento serian los más veraces.

### Título

"World Cup Russia 2018 stats and reviews"

### Descripción

El conjunto de datos contiene información sobre los partidos disputados en la copa del mundo de futbol celebrada en Rusia en 2018. Cada partido es descrito mediante un conjunto de variables cuantitativas como pueden ser por ejemplo, número de goles, faltas, tiros a puerta, etc. (stats) y por un conjunto de variables que podrían considerarse como cualitativas y que consisten en las reseñas hechas por los periodistas encargados de cubrir el evento (reviews).

### Representación gráfica

![](worldcup.png)

### Contenido

Cada registro se corresponde con un partido. Y para cada uno de ellos se han recogido los siguientes datos:

* __id__: Identificador del partido
* __name_home__: Nombre del equipo local
* __name_away__: Nombre del equipo visitante
* __code_home__: Código equipo local
* __code_away__: Código equipo visitante
* __group__: Ronda clasificatoria
* __stadium__: Estadio
* __venue__: Localización
* __datetime__: Fecha y hora
* __headline__: Titular resumen
* __summary__: Reseña neutral
* __summary_home__: Reseña del periodista local
* __summary_away__: Reseña del periodista visitante
* __goals_home__: Goles equipo local
* __goals_away__: Goles equipo visitante
* __attempts_home__: Lanzamientos equipo local
* __attempts_away__: Lanzamientos equipo visitante
* __on-target_home__: Lanzamientos entre los tres palos equipo local
* __on-target_away__: Lanzamientos entre los tres palos equipo visitante
* __off-target_home__: Lanzamientos fuera equipo local
* __off-target_away__: Lanzamientos fuera equipo visitante
* __blocked_home__: Paradas equipo local
* __blocked_away__: Paradas equipo visitante
* __woodwork_home__: Palos equipo local
* __woodwork_away__: Palos equipo visitante
* __corners_home__: Saques de esquina equipo local
* __corners_away__: Saques de esquina equipo visitante
* __offsides_home__: Fueras de juego equipo local
* __offsides_away__: Fueras de juego equipo visitante
* __ball_possession_home__: Porcentaje de posesión equipo local
* __ball_possession_away__: Porcentaje de posesión equipo visitante
* __pass_accuracy_home__: Precisión pasa equipo local
* __pass_accuracy_away__: Precisión equipo visitante
* __passes_home__: Pases equipo local
* __passes_away__: Pases equipo visitante
* __passes_completed_home__: Pases completados equipo local
* __passes_completed_away__: Pases completado equipo visitante
* __distance_covered_home__: Distancia recorrida equipo local
* __distance_covered_away__: Distancia recorrida equipo visitante
* __balls_recovered_home__: Recuperaciones equipo local
* __balls_recovered_away__: Recuperaciones equipo visitante
* __tackles_home__: Entradas equipo local
* __tackles_away__: Entradas equipo visitante
* __blocks_home__: Cortes equipo local
* __blocks_away__: Cortes equipo visitante
* __clearances_home__: Despejes equipo Local
* __clearances_away__: Despejes equipo visitante
* __yellow_cards_home__: Tarjetas amarillas equipo local
* __yellow_cards_away__: Tarjetas amarillas equipo visitante
* __direct_red_cards_home__: Tarjetas rojas directas equipo local
* __direct_red_cards_away__: Tarjetas rojas directas equipo visitante
* __indirect_red_cards_home__: Tarjetas rojas indirectas equipo local
* __indirect_red_cards_away__: Tarjetas rojas indirectas equipo visitante
* __fouls_committed_home__: Faltas equipo local
* __fouls_committed_away__: Faltas equipo visitante
* __referee_name__: Nombre del árbitro
* __referee_conrtry__: País del árbitro
* __weather_description__: Descripción del tiempo
* __weather_temperature__: Temperatura (ºC)
* __weather_windspeed__: Velocidad del viento (km/h)
* __weather_humidity__: Humedad (%)


### Agradecimientos

La propietaria de los datos es la FIFA. La Fédération Internationale de Football Association, más conocida por sus siglas __FIFA__, es la institución que gobierna las federaciones de fútbol en todo el planeta. Se fundó el 21 de mayo de 1904 y tiene su sede en Zúrich, Suiza. Forma parte del IFAB, organismo encargado de modificar las reglas del juego. Además, la FIFA organiza la Copa Mundial de Fútbol, los otros campeonatos del mundo en sus distintas categorías, ramas y variaciones de la disciplina, y los Torneos Olímpicos a la par del COI.

Me gustaría destacar la gran cantidad de información que la FIFA pone a disposición de los aficionados a través de su [web](https://www.fifa.com) y el orden y claridad con la que es presentada.

### Inspiración

El conjunto de datos podría ser utilizado en diferentes ámbitos. Algunos de ellos podrían ser:

* __Periodismo:__ Los datos podrían ser usados para, por ejemplo, realizar un reportaje sobre el mundial que sacara a relucir los datos más curiosos/destacados.

* __Almacén de datos:__ Los datos podrían ser cruzados con datos pertenecientes a otras fuentes para enriquecer un almacén de datos estadísticos.

* __Minería de datos:__ En cuanto a su uso para proyectos de minería de datos podría ser interesante estudiar:

    * __Sesgos en información:__ Podrían estudiarse la diferencias o similitudes entre las reseñas de cada uno de los periodistas (local/visitante) y la reseña neutral para extraer conclusiones sobre sesgos en el periodismo.

    * __Generador de reseñas:__ Utilizando en conjunto las variables cuantitativas y las reseñas se podría intentar construir un sistema que generase reseñas de manera automática. Aunque seguramente se necesitarían más datos, el conjunto podría ser un punto de partida para estudiar la viabilidad del proyecto.

    * __Estilos de juego:__ Podrían analizarse los diferentes estilos de juego de las selecciones (con técnicas de clustering) y estudiar cuales son los más efectivos.


### Licencia

La licencia escogida ha sido **CC0: Public Domain License**. La razón por la que he escogido esta licencia, es que todo el trabajo ha sido realizado con el único objetivo de superar la asignatura "Tipología y ciclo de vida de los datos" por lo que si de alguna forma, alguien quiere usar los datos para cualquier finalidad, esta licencia le permitirá el uso de estos con el menor número de restricciones posibles.

### Código

El código fuente se puede encontrar dentro de la carpeta "src".

### Dataset

El dataset resultante se puede encontrar en la carpeta "csv".

### Recursos

* Subirats, L., Calvo, M. (2019). Web Scraping. Editorial UOC.
* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
