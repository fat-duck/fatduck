from apscheduler.schedulers.background import BackgroundScheduler
from timetable import dl
import pytz

tz = pytz.timezone("Asia/Kuala_Lumpur")


def work():
    print("initiating dl.py...")
    dl.main()


scheduler = BackgroundScheduler()
scheduler.add_job(work, 'cron', hour=6, timezone=tz)
scheduler.start()
