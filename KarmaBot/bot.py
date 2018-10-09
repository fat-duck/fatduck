import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
from envparse import env
from timetable import prettyCSV

bot_token = env('BOT_TOKEN')
# Use a service account
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_url(method):
  return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

def process_message(update, message):
    data = {}
    data["chat_id"] = update["message"]["from"]["id"]
    data["text"] = message
    r = requests.post(get_url("sendMessage"), data=data)

def setIntakeCode(intakeCode, update):
    data = {
        u'intakeCode': intakeCode
        }
    # Add a new doc in collection 'cities' with ID 'LA'
    db.collection(u'Intake').document(str(update["message"]["from"]["id"])).set(data)

def getIntakeCode(update):
	doc_ref = db.collection(u'Intake').document(str(update["message"]["from"]["id"]))
	try:
	    doc = doc_ref.get()
	    print('Document data: {}'.format(doc.to_dict()))
	    return doc.to_dict()["intakeCode"]
	except Exception as e:
	    print('err: ' + str(e))
	    return ''

def process_update(update):
   	# print(update)
    if "/tt" in update["message"]["text"]:
        process_message(update, prettyCSV.getTimetable(getIntakeCode(update)))
    elif "/intake" in update["message"]["text"]:
        process_message(update, "Please select your intake code.")
    elif "/myint" in update["message"]["text"]:
        process_message(update, getIntakeCode(update))
    elif prettyCSV.checkIfModuleExist(str(update["message"]["text"])) and "message" in update:
    	setIntakeCode(update["message"]["text"], update)
    	process_message(update, "Your intake code is set.")
    elif "message" in update:
        process_message(update, "Hi, I am KarmaBot :)")
    return "ok!", 200