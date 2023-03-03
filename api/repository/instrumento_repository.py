import requests
from lxml import html
from models.instrumento import Instrumento
from models.tipo_instrumento import TipoInstrumento

class InstrumentoRepository:
    def __init__(self) -> None:
        pass

    def get_lecer():
        return 

    def get_mercadopago():
        # URL de la página web
        url = 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables.asp'

        try:
            # Realizamos la petición a la página web y obtenemos su contenido HTML
            response = requests.get(url)
            response.raise_for_status()
            content = response.content

            # Parseamos el contenido HTML con la librería lxml y obtenemos el objeto 'Element'
            parsed_content = html.fromstring(content)

            # Obtenemos el título de la página web usando XPath
            value = parsed_content.xpath('/html/body/div/div[2]/div/div/div/div/table/tbody/tr[10]/td[3]')[0]

            # Imprimimos el título de la página web
            print('El título de la página es:', value.text)
            plazo_fijo = Instrumento("Plazo Fijo", TipoInstrumento.PlazoFijo.value, value.text)
            json_data = plazo_fijo.to_json()
            return json_data
        
        except requests.exceptions.HTTPError as e:
            print('Ocurrió un error al obtener la página:', e)
        except requests.exceptions.RequestException as e:
            print('Ocurrió un error al realizar la petición:', e)
        except Exception as e:
            print('Ocurrió un error inesperado:', e)