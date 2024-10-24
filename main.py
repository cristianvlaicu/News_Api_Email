# We are going to create a program that will send us a daily email with news about a topic of our choice.
# An API will be used to gather this information.

import requests  # with this library we are going to access that API to gather the information.
from send_email import send_email

topic = "apple"  # we create the topic variable to choose the topic about which it will send us an email.

api_key = "0df5ef5a18d64fcd88136b3f2349b948"
url = (
    "https://newsapi.org/v2/everything?"
    f"q={topic}&"
    "from=2024-10-23&to=2024-10-23&sortBy=popularity&"
    "apiKey=0df5ef5a18d64fcd88136b3f2349b948&"
    "language=es"
)  # we choose the language of the news that the program will send us to the email.

request = requests.get(
    url
)  # we request the url with the API format so that our computer can read it.
content = (
    request.json()
)  # and after reading it we save the text in a variable of type string. By putting .json that variable becomes a dictionary type.

body = ""  # we create the body of the email as a string.

# We iterate one by one through the articles that are in the dictionary contect previously created, within the articles key.
for article in content["articles"][:20]:
    if (
        article["title"] is not None
    ):  # with the conditional we ensure that it sends the real articles, with a title and does not send me anything else.
        body = (
            body
            + article["title"]
            + "\n"
            + article["description"]
            + "\n"
            + article["url"]
            + 2 * "\n"
        )

# If we want the subject to be put correctly in the email we receive, we must create the email message outside the for loop because otherwise
# it is understood that there are 20 different subjects and it is considered spam (Gmail blocks it and does not send it).
message = f"""\
Subject: Today's news:


{body}
    """

message = message.encode(
    "UTF-8"
)  # we encode the message in the same code that the interpreter uses so that it can be read correctly when we receive it.

# We call the send_email function created in previous applications to send us the email.
send_email(message)