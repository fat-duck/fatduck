from envparse import env
from flask import Flask, request
from telegram_bot import bot
from telegram_bot import webhook
from timetable import scheduler
env.read_envfile()

app = Flask(__name__)

bot_token = env('BOT_TOKEN')

scheduler
webhook


@app.route("/{}".format(bot_token), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        print(update)
        bot.process_update(update)
        return "ok!", 200


if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        debug=None,
        load_dotenv=True)
