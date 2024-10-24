    # Vamos a crear un programa que nos va a mandar un email al día con noticias sobre un tema que elijamos. Se usará una API para recolectar esa información.

import requests  # con esta librería vamos a acceder a esa API para recolectar la información.

apy_key = "0df5ef5a18d64fcd88136b3f2349b948"
url = "https://newsapi.org/v2/everything?q=apple&" \
       "from=2024-10-23&to=2024-10-23&sortBy=popularity&apiKey=" \
       "0df5ef5a18d64fcd88136b3f2349b948"

request = requests.get(url)  # requerimos la url con el formato API para que nuestro ordenador pueda leerlo.
content = request.json()     # y después de leerlo guardamos el texto en una variable del tipo string. Al poner .json esa variable pasa a ser del tipo diccionario.

# Recorremos de uno en uno los artículos que hay en el diccionario contect antes creado, dentro de la clave articles.
for article in content['articles']:
    print(article['title'])
    print(article['description'])