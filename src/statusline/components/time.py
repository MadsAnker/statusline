from datetime import datetime

def getTime():
    now = datetime.now()
    return now.strftime("{}  (Week %W) %d-%m   {} %H:%M".format("", ""))
