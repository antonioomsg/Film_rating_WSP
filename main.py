
import argparse
import pandas as pd
from functions import *
from functools import reduce 



parser = argparse.ArgumentParser(description="Introduce diferentes variables para hallar las top peliculas según tu elección")


parser.add_argument("-c" "--categoria",help="Este valor corresponde al numero de resultados que quieres ver por pantalla",dest="genero",type=str)
parser.add_argument("-a" "--año", help="Introduce un año y te dire cuales son las top peliculas de ese año",dest="ano",type=int)
parser.add_argument("-n" "--n_resultados", help="introduce el numero de peliculas que te gustaría que saliesen por pantalla",dest="num",type=int)

args=parser.parse_args()

def main():
    print(filtrapeliculas(args.genero,args.ano,args.num))
    imprime()

if __name__=="__main__":
    main()


