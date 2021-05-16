from apscheduler.schedulers.background import BackgroundScheduler

from django.conf import settings

scheduler = BackgroundScheduler()

def start_job1():

    if settings.STATUS_JOB1 == True:
        pass
    else:
        settings.JOB1 = scheduler.add_job(tarea_job1, 'interval', seconds=3) 
        scheduler.start()
        settings.STATUS_JOB1 = True

def stop_job1():

    if settings.STATUS_JOB1 == True:
        settings.JOB1.resume()
        settings.STATUS_JOB1 = False


def tarea_job1():
    settings.CONTADOR = settings.CONTADOR + 1


