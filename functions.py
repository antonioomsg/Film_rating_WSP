from argparse import ArgumentParser
import pandas as pd
from functools import reduce 
import requests
import os
from dotenv import load_dotenv
load_dotenv()
import urllib.parse
import requests
import webbrowser
from gtts import gTTS
import subprocess


apiKey = os.getenv("ap_film")

def drop_null(table,subset):
    table.dropna(subset=[f"{subset}"],inplace=True)

df = pd.read_csv("Data_Source/Conpopularity1.csv")

def filtrapeliculas(genero,ano,num_dislp):
    filterinfDataframe = df[(df['genero'] == f"{genero}") & (df['año'] == ano) ].sort_values(by=['popularidad'],ascending=False).head(num_dislp)
    filterinfDataframe = filterinfDataframe.reset_index(drop=True)
    return filterinfDataframe


def actualiza_valor_fila(tabla,fila_valor,fila,columna,valor):
    tabla.loc[tabla[f"{fila_valor}"]== fila,columna]= valor

def imprime():
    count=0
    subprocess.run(["say", "Te gustaría ver el trailer de alguna de estas peliculas, responde si o no"])
    print("Te gustaría ver el trailer de alguna de estas peliculas, responde si o no")
    respuesta =input()
    if respuesta == "si":
        subprocess.run(["say", "Por favor dame el nombre de la pelicula"])
        print("Por favor dame el nombre de la pelicula")
        nombrepeli=input()
        busca1(apiKey,urllib.parse.quote(f"{nombrepeli}"))
        try:
            busca_trailer(id_data,apiKey)
            pass
        except:
            subprocess.run(["say", "No tengo trailer para esta pelicula, haz algún research en youtube"])   
            subprocess.run(["say", "¿Te gustaría ver el trailer de alguna otra pelicula?"])
            respuesta=input()
            if respuesta =="si":
                    try:
                        subprocess.run(["say", "Por favor dame el nombre de la pelicula"])
                        nombrepeli=input()
                        busca1(apiKey,urllib.parse.quote(f"{nombrepeli}"))
                        busca_trailer(id_data,apiKey)
                        count+=1
                        pass
                    except:
                        if count ==2:
                            subprocess.run(["say", "No ha sido posible"])
                            subprocess.run(["say", "¿Te gustaría ver el trailer de alguna otra pelicula?"])
                            count+=1
                            print("count")
                            respuesta=input()
                        else:
                            subprocess.run(["say", "¡Deja de ponerme a prueba por favor!"])
            
            subprocess.run(["say", "Nos vemos en otra"])
            

    else:
        subprocess.run(["say", "Perfecto nos vemos en otra"])
        print("Lo que mandes, aquí estoy para tu proxima pelicula")

def busca1(key,film_name):
    url = "https://api.themoviedb.org/3/search/movie?api_key="+key+"&language=en-US&query="+film_name
    res = requests.get(url)
    jason = res.json()
    global id_data
    id_data = jason["results"][0]["id"]
    return id_data

def busca(key,film_name):
    url = "https://api.themoviedb.org/3/search/movie?api_key="+key+"&language=en-US&query="+film_name
    res = requests.get(url)
    print(url)
    return res.json()

def busca_trailer(id_peli,key):
    url = "https://api.themoviedb.org/3/movie/"+f"{id_peli}"+"/videos?api_key="+key+"&language=en-US"
    res = requests.get(url)
    jason = res.json()
    id_trailer = jason["results"][1]["key"]
    print(id_trailer)
    print("https://www.youtube.com/watch?v="+id_trailer)
    webbrowser.open("https://www.youtube.com/watch?v="+id_trailer)