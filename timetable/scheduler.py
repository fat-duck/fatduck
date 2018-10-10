from apscheduler.schedulers.background import BackgroundScheduler
from timetable import dl


def work():
    print("initiating dl.py...")
    dl.main()


scheduler = BackgroundScheduler()
scheduler.add_job(work, 'cron', hour=6)
scheduler.start()
