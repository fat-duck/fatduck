import requests
from envparse import env
from timetable import prettyCSV
from flask import Flask, request

env.read_envfile()

app = Flask(__name__)

bot_token = env('BOT_TOKEN')

def get_url(method):
  return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

def process_message(update, message):
    data = {}
    data["chat_id"] = update["message"]["from"]["id"]
    data["text"] = message
    r = requests.post(get_url("sendMessage"), data=data)

@app.route("/{}".format(bot_token), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        # print(update)
        if "/tt" in update["message"]["text"] and "message" in update :
            process_message(update, prettyCSV.getTimetable())
        elif "message" in update:
            process_message(update, "Hi, I am KarmaBot :)")
        return "ok!", 200