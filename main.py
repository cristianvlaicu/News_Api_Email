    # Vamos a crear un programa que nos va a mandar un email al día con noticias sobre un tema que elijamos. Se usará una API para recolectar esa información.

import requests  # con esta librería vamos a acceder a esa API para recolectar la información.
from send_email import send_email

apy_key = "0df5ef5a18d64fcd88136b3f2349b948"
url = "https://newsapi.org/v2/everything?q=apple&" \
       "from=2024-10-23&to=2024-10-23&sortBy=popularity&apiKey=" \
       "0df5ef5a18d64fcd88136b3f2349b948"

request = requests.get(url)  # requerimos la url con el formato API para que nuestro ordenador pueda leerlo.
content = request.json()     # y después de leerlo guardamos el texto en una variable del tipo string. Al poner .json esa variable pasa a ser del tipo diccionario.

# Recorremos de uno en uno los artículos que hay en el diccionario contect antes creado, dentro de la clave articles.
body = ""
for article in content['articles']:
    if article['title'] is not None:  # con el condicional aseguramos que enviar los artículos de verdad, con título y no me mande otra cosa.
        body = body + article['title'] + "\n" + article['description'] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)