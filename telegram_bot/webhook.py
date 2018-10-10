from pprint import pprint
from envparse import env
import requests

env.read_envfile()

bot_token = env('BOT_TOKEN')
test_url = env('BOT_TEST_URL') + "/{}".format(bot_token)
print(env('BOT_TEST_URL'))


def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token, method)


r = requests.get(get_url("setWebhook"), data={"url": test_url})
r = requests.get(get_url("getWebhookInfo"))
pprint(r.status_code)
pprint(r.json())
