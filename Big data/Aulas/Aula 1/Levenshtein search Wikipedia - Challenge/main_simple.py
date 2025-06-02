from multiprocessing import Pool
import math as mt
import re
import os

SEARCH = 'data'

folder_data = "./WikipediaTI"
list_data = os.listdir(folder_data)

def levenshteinDistance(str1, str2):
    
    #    +======================+
    #   || Implemente a função ||
    #   +======================+

    return None


def process(data):

    for wikipage in data:
        with open(f'{folder_data}/{wikipage}', 'r', encoding='utf-8') as arq:
            htmlstring = arq.read()

        #    +====================================+
        #   || Limpe as tags HTML de htmlstring  ||
        #   +====================================+
    
    return None

results = process(list_data)
with open('result.txt', 'w', encoding='utf-8') as result:
    for score in results:
        result.write(f'{score[0].replace(' - Wikipedia.html', '')} \t : {score[1]}\n')