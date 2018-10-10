from apscheduler.schedulers.background import BackgroundScheduler
from timetable import dl
from pytz import utc
import datetime


def work():
    print("initiating dl.py...")
    dl.main()


scheduler = BackgroundScheduler()
scheduler.add_job(work, 'interval', seconds=10)
scheduler.start()
