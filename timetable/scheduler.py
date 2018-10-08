import schedule
import dl
import time


def job():
    dl.main()


schedule.every(6).hour.do(job)
schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
