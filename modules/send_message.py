import requests
import json

class SendMessage:

    def __init__(self) -> None:
        with open('./config/config.json') as f:
            self.config = json.load(f)

    def tel_send_message(self,chat_id, text):
        url = f'https://api.telegram.org/bot{self.config["TOKEN"]}/sendMessage'
        payload = {
                    'chat_id': chat_id,
                    'text': text
                    }
    
        r = requests.post(url,json=payload)
        return r


    def send_image(self,chat_id):
        url = f'https://api.telegram.org/bot{self.config["TOKEN"]}/sendPhoto'
        files = {'photo': open('./image.png', 'rb')}
        data = {'chat_id' : chat_id}
        r= requests.post(url, files=files, data=data)

    def tel_send_image(self,chat_id,base64):
        url = f'https://api.telegram.org/bot{self.config["TOKEN"]}/sendPhoto'
        payload = {
                    'chat_id': chat_id,"photo":base64
        }
        # print(payload)
        # files = {
            
        # }
        r = requests.post(url,json=payload)
        print(r.status_code, r.reason, r.content)
        return r