from apscheduler.schedulers.background import BackgroundScheduler
from timetable import dl
import pytz

tz = pytz.timezone("Asia/Kuala_Lumpur")
dl.main()  # Run download at least once before starting the app


def work():
    print("initiating dl.py...")
    try:
        dl.main()
        return "Download initiated"
    except Exception as e:
        raise e


scheduler = BackgroundScheduler()
scheduler.add_job(work, 'cron', hour=6, timezone=tz)
scheduler.start()
