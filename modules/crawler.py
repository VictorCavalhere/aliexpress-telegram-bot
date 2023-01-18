import time
import os.path
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from modules.send_message import SendMessage
import base64

## Setup chrome options
def crawler(chat_id):
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")

    # Set path to chromedriver as per your configuration
    homedir = os.path.expanduser("~")
    webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

    # Choose Chrome Browser
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Get page
    browser.get("https://pt.aliexpress.com/?spm=a2g0o.home.1000002.1.30411c91SLyjdc&gatewayAdapt=glo2bra")
    Y = 0
    for i in range(0,10):
        browser.execute_script(f"window.scrollTo(0, {Y})") 
        Y +=100

    browser.find_element(By.XPATH,'//*[@id="root"]/div[4]/div/div[2]/ul[2]/li[1]/a/div').click()
    time.sleep(5)
    send_message = SendMessage()
    
    for idx in range(1,10):
        print(f'//*[@id="recyclerview"]/div/div[5]/div/div[{idx}]')
        text_of_item = browser.find_element(By.XPATH,f'//*[@id="recyclerview"]/div/div[5]/div/div[{idx}]').text
        values = re.findall(r'R\$\s(\d+\,\d{2})',text_of_item)
        list_of_values = []
        for value in values:
            list_of_values.append(float(value.replace(",",".")))
        min_value = min(list_of_values)
        max_value = max(list_of_values)
        image = browser.find_element(By.XPATH,f'//*[@id="recyclerview"]/div/div[5]/div/div[{idx}]').screenshot_as_base64
        decoded_data=base64.b64decode((image))
        #write the decoded data back to original format in  file
        img_file = open('./image.png', 'wb')
        img_file.write(decoded_data)
        img_file.close()
        send_message.send_image(chat_id)
        send_message.tel_send_message(chat_id,f"De: R$ {str(max_value)} Por: R$ {str(min_value)}")
        



