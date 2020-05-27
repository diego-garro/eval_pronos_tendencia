#!/usr/bin/python3
#-*-coding: utf-8-*-

__author__ = "Diego Antonio Garro Molina"
__copyright__ = "Copyright 2019, Diego Garro e Instituto Meteorológico Nacional"
__credits__ = "Diego Garro, Instituto Meteorologico Nacional"
__license__ = "None"
__version__ = "1.0.2"
__maintaier__ = "Diego Garro Molina"
__email__ = "dgarro@imn.ac.cr"
__status__ = "Developer"

import requests
import re
from bs4 import BeautifulSoup

def extraer_metar(filename):
    formato = r'\d{12}'
    f2 = open('test/prueba.txt', 'w')
    with open(filename) as f:
        metar = []
        for linea in f:
            acierto = re.match(formato, linea)
            acierto_espacios = re.match(r'\s{2,}', linea)
            if acierto:
                metar.append(linea.replace('\n', ''))
            elif acierto_espacios:
                metar.append(re.sub(r'\s{2,}', " ", linea).replace('\n', ''))
            else:
                continue
            
            for elemento in metar:
                if elemento.count('=') > 0:
                    f2.write(''.join(metar) + '\n')
                    metar = []
    f2.close()

def scrap_metar(url):
    """
    Esta función scrapea la página de Ogimet.com para obtener el último METAR emitido
    por MROC.
    -----------------------
    Recibe dos parámetros.
    url: string, la dirección de Ogimet.com de donde se extraerá el METAR más reciente.
    -----------------------
    Retorna el METAR más actual como una cadena de texto si logra conectar a la url,
    si no, retorna una cadena vacía
    """
    f = open("texto_web.txt", 'w')
    req = requests.get(url)
    statusCode = req.status_code
    if statusCode == 200:
        html = BeautifulSoup(req.text, "html.parser")
        entrada = html.find('pre')
        f.write(str(entrada))
    else:
        return ''
    f.close()

    # Se abre de nuevo el archivo texto_web.txt para extraer el METAR
    extraer_metar("texto_web.txt")