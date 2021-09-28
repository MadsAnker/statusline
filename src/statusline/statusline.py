from . import components

def getStatusLine():
    time = components.time.getTime()
    battery = components.battery.getBatteryStatus()
    sound = components.sound.getVolumne()
    wifi = components.wifi.getWifiStatus()
    nextTask = components.tasks.getNextTask()
    nextEvent = components.calendar.getNextEvent()

    return "{}   {}   {}   {}   {}   {}".format(nextEvent, nextTask, wifi, sound, battery, time)
