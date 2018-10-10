from envparse import env
from flask import Flask, request
import bot

env.read_envfile()

app = Flask(__name__)

bot_token = env('BOT_TOKEN')


@app.route("/{}".format(bot_token), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        print(update)
        bot.process_update(update)
        # # print(update)
        # if "/tt" in update["message"]["text"]:
        #     bot.process_message(update, prettyCSV.getTimetable())
        # elif "/intake" in update["message"]["text"]:
        #     process_message(update, "Please select your intake code.")
        # elif "message" in update:
        #     process_message(update, "Hi, I am KarmaBot :)")
        return "ok!", 200
