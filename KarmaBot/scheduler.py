from apscheduler.schedulers.blocking import BlockingScheduler
import pytz, dl

def job_function():
    dl.main()

sched = BlockingScheduler()

tz = pytz.timezone('Asia/Kuala_Lumpur')

sched.add_job(job_function, 'cron', hour='01', minute='44', timezone=tz)

# while True:
#     schedule.run_pending()
#     time.sleep(60)

sched.start()