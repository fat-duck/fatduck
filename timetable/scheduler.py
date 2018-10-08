import schedule
import dl
import time


def job():
    print("initiating dl.py...")
    dl.main()


schedule.every(6).hours.do(job)
# schedule.every().minute.do(job)

while True:
    print("Scheduler running . . . . . ")
    schedule.run_pending()
    time.sleep(60)
