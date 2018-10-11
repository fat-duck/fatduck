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
# Get count of pending updates when the server deploys
pendingUpdateCount = webhook.getPendingUpdateCount()[
    "result"]["pending_update_count"]


@app.route("/{}".format(bot_token), methods=["POST"])
def process_update():
    if request.method == "POST":
        global pendingUpdateCount  # To amend it globally
        update = request.get_json()
        # Set the pending update count to firebase
        bot.setPendingUpdateCount(pendingUpdateCount, update)
        userPendingUpdateCount = bot.getPendingUpdateCount(update)  # Get
        if userPendingUpdateCount <= 1:  # All the pending update can only send once
            print(update)
            bot.process_update(update)
        else:
            print(update)
        pendingUpdateCount -= 1  # After process one request minus one
        return "ok!", 200


if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        debug=None,
        load_dotenv=True)
