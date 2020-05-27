"""
Script principal del software para la evaluación de los pronósticos de tendencia.
"""

from utils.scrap_tools import scrap_metar

URL_BASE = 'https://www.ogimet.com/display_metars2.php?lugar=mroc&tipo=SA&ord=REV&nil=SI&fmt=txt&ano={}&mes={}&day={}&hora={}&anof={}&mesf={}&dayf={}&horaf={}&minf=05&enviar=Ver'
url = "https://www.ogimet.com/display_metars2.php?lugar=mroc&tipo=SA&ord=DIR&nil=SI&fmt=txt&ano=2020&mes=05&day=26&hora=05&anof=2020&mesf=05&dayf=27&horaf=05&minf=59&enviar=Ver"
# url = URL_BASE.format(hoy[0], str(hoy[1]).zfill(2), str(hoy[2]).zfill(2), str(hoy[3]).zfill(2), hoy[0], str(hoy[1]).zfill(2), str(hoy[2]).zfill(2), str(hoy[3]).zfill(2))

scrap_metar(url)