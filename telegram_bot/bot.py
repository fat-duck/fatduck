import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import re
from envparse import env
from reader import prettyCSV

env.read_envfile()
bot_token = env('BOT_TOKEN')

# Use a service account
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

regex_tt = re.compile('\/tt[1-6]')


def setPendingUpdateCount(cnt, update):
    data = {
        u'pending_update_count': cnt
    }

    db.collection(u'Update').document(
        str(update["message"]["from"]["id"])).set(data)


def getPendingUpdateCount(update):
    doc_ref = db.collection(u'Update').document(
        str(update["message"]["from"]["id"]))
    try:
        doc = doc_ref.get()
        print('Document data: {}'.format(doc.to_dict()))
        return doc.to_dict()["pending_update_count"]
    except Exception as e:
        print('err: ' + str(e))
        return ''


def setSessionCode(code, update):
    data = {
        u'sessionCode': code
    }

    db.collection(u'Session').document(
        str(update["message"]["from"]["id"])).set(data)


def getSessionCode(update):
    doc_ref = db.collection(u'Session').document(
        str(update["message"]["from"]["id"]))
    try:
        doc = doc_ref.get()
        print('Document data: {}'.format(doc.to_dict()))
        return doc.to_dict()["sessionCode"]
    except Exception as e:
        print('err: ' + str(e))
        return ''

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token, method)


def process_message(update, message):
    data = {}
    data["chat_id"] = update["message"]["from"]["id"]
    data["text"] = message
    r = requests.post(get_url("sendMessage"), data=data)


def process_html_message(update, message):
    data = {}
    data["chat_id"] = update["message"]["from"]["id"]
    data["text"] = message
    data["parse_mode"] = 'HTML'
    r = requests.post(get_url("sendMessage"), data=data)


def setIntakeCode(intakeCode, update):
    data = {
        u'intakeCode': intakeCode
    }

    db.collection(u'Intake').document(
        str(update["message"]["from"]["id"])).set(data)


def getIntakeCode(update):
    doc_ref = db.collection(u'Intake').document(
        str(update["message"]["from"]["id"]))
    try:
        doc = doc_ref.get()
        print('Document data: {}'.format(doc.to_dict()))
        return doc.to_dict()["intakeCode"]
    except Exception as e:
        print('err: ' + str(e))
        return ''


def process_update(update):
    # print(update)
    if "/start" == update["message"]["text"]:
        setSessionCode('start', update)
        process_message(update, "Hi, nice to meet you.")

    elif "/tt" == update["message"]["text"]:
        if (getIntakeCode(update) != ''):
            process_html_message(
                update, prettyCSV.getTimetable(getIntakeCode(update)))
        else:
            process_html_message(
                update, "Please set your intake code with /setintake first.")
        setSessionCode('tt', update)

    elif regex_tt.match(update["message"]["text"]) != None:
        if (getIntakeCode(update) != ''):
            process_html_message(update, prettyCSV.getDayTimetable(getIntakeCode(
                update), regex_tt.match(update["message"]["text"]).group().replace('/tt', '')))
        else:
            process_html_message(
                update, "Please set your intake code with /setintake first.")
        setSessionCode('tt', update)

    elif "/setintake" == update["message"]["text"]:
        setSessionCode('setintakecode', update)
        process_message(update, "Please select your intake code.")

    elif getSessionCode(update) == 'setintakecode':
        if(prettyCSV.checkIfModuleExist(str(update["message"]["text"]))):
            setIntakeCode(update["message"]["text"].upper(), update)
            process_message(update, "Your intake code is set.")
            setSessionCode('start', update)
        else:
            process_message(update, "Intake code is invalid.")
            setSessionCode('start', update)

    elif "/showintake" in update["message"]["text"]:
        setSessionCode('showintake', update)
        process_message(update, getIntakeCode(update))

    elif "message" in update:
        setSessionCode('start', update)
        process_message(update, "Hi, I am TT Bot :)")

    return "ok!", 200
