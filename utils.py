import importlib
from job_manager.models import App


def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)


def manage_jobs(app_id):
    try:
        app_detail = App.objects.get(pk=app_id)
    except App.DoesNotExist:
        return False
    module = app_detail.name + '.' + app_detail.module
    Job = import_from(module, app_detail.object)
    try:
        job_detail = Job.objects.get(pk=1)
    except Job.DoesNotExist:
        return False
    print(job_detail.name)
    return True
