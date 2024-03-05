from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
import re
import time
#============呼叫檔案內容============
from linebot.models import *
from eventlist import *
from flex_message import *
from APILINK import *
from OpenAI_0105 import *
#====================================
import re
import time


app = Flask(__name__)

#======================   Expokit 主辦方   ======================
CHANNEL_ACCESS_TOKEN = 'oAWBta6I8AmQmrG3gH4jjkFN0FWRg2UmSSb8Vms1YiRxvyjF2ltWvMTxyZtkwGr1VWW4uW6Y8NL/+3zDyMVUuItEZohC1Tdl1JZBqwQ/ZOy+uhBBty8PQf+OhZm0SlG+GUTj5MBeYITS1n6WWIUwOAdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '664a451c7b810dea8005fddf69f27053'
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# 監聽所有來自 /callback 的 Post Request
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

#自動回應訊息
@handler.add(MessageEvent, message = TextMessage)
def handle_text_message(event):
    msg = event.message.text
    user_id = event.source.user_id
    pattern = re.compile(r'^/', re.IGNORECASE)
    
    #LCIA
    if msg == "會員資料":
        reply = TextSendMessage(text = "很抱歉，我不明白您的問題。您可以問我其他的問題。")
    line_bot_api.reply_message(event.reply_token, reply)
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
