    # Creamos el módulo que nos manda el email cada vez que un usuario rellena y envía el formulario de contacto. Es para ser llamado por Contact_Me.

import smtplib, ssl  # librería que crea una sesion de email para los clientes.
import os

def send_email(message):     # creamos función/módulo para poder llamarla desde la página Contact_Me.
    host = "smtp.gmail.com"  # "este es quien" manda el email (con el formulario rellenado del usuario)
    port = 465

    username = "lordbeilish13@gmail.com"   # el que manda el email, va a iniciar sesión en nuestra cuenta...
    password = os.getenv("password")
    receiver = "dkelnumero1@gmail.com"      #... para (auto)mandar el email del usuario (es como si nos mandamos un autoemail con el mensaje y los datos del usuario que nos contacta en la página).
    context = ssl.create_default_context()  # este es un contexto seguro que viene incorporado para mandar los emails de forma segura.

    with smtplib.SMTP_SSL(host, port, context=context) as server:  # este es el "programa-servidor" que manda el email de forma automática.
        server.login(username, password)
        server.sendmail(username, receiver, message)