from envparse import env
from flask import Flask, request
from telegram_bot import bot
from timetable import scheduler
env.read_envfile()

app = Flask(__name__)

bot_token = env('BOT_TOKEN')

scheduler


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


if __name__ == '__main__':

    app.run(
        host='localhost',
        port='5000',
        debug=None,
        load_dotenv=True)
