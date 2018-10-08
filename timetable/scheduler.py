import schedule
from timetable import dl
#import multiprocessing as mp


def job():
    print("initiating dl.py...")
    dl.main()


def main(job):

    schedule.every(1).second.do(job)
    schedule.every(6).hours.do(job)
    print("Scheduler running . . . . . ")
    schedule.run_pending()


# schedule.every().minute.do(job)


#dl.main()  # will run at least once before passing on to scheduler
#main(job)
