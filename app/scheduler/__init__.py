from app.scheduler.create_random_post import *
from apscheduler.schedulers.background import BackgroundScheduler


def cron_jobs():
    print("JOB Started")
    sched = BackgroundScheduler()
    sched.add_job(create_random_post, "interval", minutes=1)

    sched.start()
