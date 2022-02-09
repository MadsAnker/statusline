from icalevents.icalevents import events
from datetime import datetime, timedelta
from pytz import timezone
from dateutil.relativedelta import relativedelta
import re
from os.path import exists
import json

#
# Returns a string representation of the next calendar event 
# from itslearning
#
def getNextEvent():
    DM = events("webcal://sdu.itslearning.com/Calendar/CalendarFeed.ashx?LocationType=3&LocationID=0&PersonId=444609&CustomerId=900937&ChildId=0&Guid=2f3f48998ee593a66c64c1e64243e178&Culture=en-GB&FavoriteOnly=True", fix_apple=True)
    #Find the first event that has not yet started
    startIndex = 0
    while (startIndex < len(DM) and hasStarted(DM[startIndex])):
           startIndex += 1

    #Return a string representation of the event
    if (startIndex < len(DM)):
        return "{}  {}".format("", getText(DM[startIndex]))
    else:
        return ""

#
# Returns a string represenation of a given event
#
def getText(event):
    courses = {
        "DM549": "Discrete mathematics",
        "DM561": "Linear algebra",
        "DM534": "Introction to computer science",
        "DM572": "Networks and cybersecurity",
        "DM550": "Introduction to programming",
        "DM500": "Studieintroduktion",
        "DM507": "Algorithms and datastructures",
        "DM552": "Programming languages",
        "DM510": "Operating systems",
        "DM563": "Concurrent programming",
        "DM505": "Databases",
        "": "undefined"
    }

    #Store title of the event
    title = str(event.summary)

    #Extract room number
    room = "No room"
    roomMatches = re.search("Odense (U.*)", title)
    if (roomMatches):
        room = roomMatches.group(1)

    #Extract course number
    course = ""
    courseMatches = re.search("(DM\d+)", title)
    if (courseMatches):
        course = courses[courseMatches.group(1)]

    #Compose and return string
    return "{} - {}  ({})".format(room, course, displayTime(event))

#
# Gets a string representation of the relative start time
# of an event in (somewhat) natural language
#
def displayTime(event):
    #Initialize time variables
    tz = timezone('Europe/Copenhagen')
    start = event.start.astimezone(tz)
    now = datetime.now(tz)
    tomorrow = now + timedelta(days=1)

    #None/tomorrow/Day
    dayString = None
    if (now.date() == start.date()):
        dayString = ""
    elif (tomorrow.date() == start.date()):
        dayString = "tomorrow"
    else:
        dayString = start.strftime("%A")

    if (dayString):
        return start.strftime("{} at %H:%M").format(dayString)

    return start.strftime("%H:%M")

#
# Returns true if the event has started at least 15 min ago
#
def hasStarted(event):
    now = datetime.now().timestamp()
    start = event.start.timestamp()
    return (now-start >= 15*60)
