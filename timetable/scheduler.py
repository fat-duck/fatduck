from apscheduler.schedulers.background import BackgroundScheduler
import dl
from pytz import utc
import time


def work():
    print("initiating dl.py...")
    dl.main()


scheduler = BackgroundScheduler()
scheduler.add_job(work, 'interval', seconds=10)
scheduler.start()
try:
    while True:
        time.sleep(5)
except(KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
