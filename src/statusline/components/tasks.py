import subprocess
import re
from taskw import TaskWarrior
from datetime import datetime

def getNextTask():
    w = TaskWarrior()
    tasks = w.load_tasks()
    pending = tasks['pending']
    if (len(pending) == 0):
        return "No upcoming tasks"
    pending.sort(key=lambda x: -x['urgency'])
    nextTask = pending[0]
    if ('due' in nextTask):
        dueDate = datetime.fromisoformat("{}-{}-{}".format(nextTask['due'][:4], nextTask['due'][4:6], nextTask['due'][6:8]))
        return "{}  Next task (due {}): {}".format("", dueDate.strftime("%d-%m"), nextTask['description'])
    else:
        return "{}  Next task: {}".format("", nextTask['description'])

