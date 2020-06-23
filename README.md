# Film_rating_WSP

## Rating peliculas por popularidad.
***
## Trabajo realizado:

He descargado una base de datos en kaggle que posteriormente hemos enriquezido con la appi de "The Movie DB" 

He enriquecido la base de datos de kaggle con la API de TMDB para poder hallar y organizar los resultados de busqueda por popularidad. 
La popularidad según nuestra api se basa en:

 Numero de votos dento de TMDB.
 Numero de visitas dentro de TMDB.
 Numero de personas que la marcan como favoritas en el día.
 Numero de personas que la añaden a su lista de reproducción.
 Puntuación anterior.

## ¿Como se utiliza?:

Desde la terminal ejecuta el programa. 

Debes introducir los siguientes parametros para que el programa funcione. 

* -c Es el genero de las peliculas que te gustaría ver.
    
    -Drama
    -Romantic
    -Comedy
    -Crime
    -Thriller
    -Adventure
    -Documentary
    -Horror
    -Action
    -Western
    -Spy
    -History
    -Biography
    -Musical
    -Fantasy
    -War
    -Grotesque
    -Gangster
    -Animation
    -Mythology
    -Noir
    -Super-hero
    -Biblical
    -Sport
    -Sperimental
    -Short Movie

* -a Filtra por año las peliculas que salen por pantalla.
    
    - Puedes ver peliculas desde el año 1909 hasta el 2019

* -n Número de peliculas que te gustaría que el programa te diese por pantalla. 


## Recursos utilizados: 
    - Pandas
    - Python
    - Requests
    - Argparse
    - subprocess
    - webbrowser

![Alt Text](https://github.com/antonioomsg/Film_rating_WSP/blob/master/popcorn.gif)
