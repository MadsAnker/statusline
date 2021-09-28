import subprocess
import re

def getBatteryStatus():
    try:
        response = subprocess.run(["sudo", "tlp-stat", "-b"], capture_output=True, encoding="utf-8")
        match = re.search("Charge total[^\d]+?([\d\.]+)", response.stdout)
        val = float(match.group(1))
        icon = ""
        if (val < 25-12):
            icon = ""
        elif (val < 50-12):
            icon = ""
        elif (val < 75-12):
            icon = ""
        elif (val < 100-12):
            icon = ""
        else:
            icon = ""
        return " {} {}% ".format(icon, val)
    except:
        return ""
