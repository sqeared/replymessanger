# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

#Channel Access Token
line_bot_api = LineBotApi('BotMZmLEcw0LfOe3ONBpCTcq+BlHcOD8zxzVz5tETYfKR4HCJW8y60bzCp3+7G4aT21Y1GICgmvPpdPsaEFVeXH4AvWTob8rPdBFnkKJgDed6uHVTVNZ6S7/FXl5SO82V+rA9YdS8fMI66T/OIc5rAdB04t89/1O/w1cDnyilFU=')
#Channel Secret
handler = WebhookHandler('dd2faab72a1b69f1843244b56f69117f')

line_bot_api.push_message('Ue5a33ec4d43958a17917c57eecfc088f', TextSendMessage(text='Are you ready?'))


 #/callback Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

 

##### function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)