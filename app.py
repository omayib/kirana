from crypt import methods
from urllib import response
import pandas as pd
from waitress import serve
import os
from kiranaengine import *
from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

kiraengine = None
base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data")
faqlist = [os.path.join(base_path,"sapaan.tsv"),
            os.path.join(base_path,"faq.tsv"),
            os.path.join(base_path,"agent.tsv"),]
kiranaengine = KiranaEngine(faqlist)
    

def get_response(user_message):
    return kiranaengine.query(user_message)

@app.route("/chat",methods=["POST"])
def start_chat():
    try:
        user_message_json = request.get_json()
        print("req json: "+str(user_message_json['text']))
        user_message=user_message_json['text']
        kirana_message = get_response(user_message)
        return jsonify({"response":kirana_message})
    except Exception as e :
        print(e)
        return jsonify({"response":"Maaf saya belum memahami😊. Ulangi dengan sederhana ya..🙏"})

    

if __name__ == "__main__":
    # app.run(port=8080)
    serve(app,host='0.0.0.0', port=80)

