from flask import Flask
from flask import request
from flask import Response
import requests
from modules.crawler import crawler
app = Flask(__name__)
 
def tel_parse_message(message):
    print("message-->",message)
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        print("txt-->", txt)
 
        return chat_id,txt
    except:
        print("NO text found-->>")


@ app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        chat_id, txt = tel_parse_message(msg)
        crawler(chat_id)
        return "<h1>Welcome!</h1>"
           
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
    app.run(threaded=True)