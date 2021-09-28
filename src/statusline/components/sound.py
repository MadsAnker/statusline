import subprocess
import re

def getVolumne():
    response = subprocess.run(["amixer", "get", "Master"], encoding="utf-8", capture_output=True)
    match = re.search("\[(\d+)%\]", response.stdout)
    val = int(match.group(1))
    icon = ""
    if (val == 0):
        icon = ""
    elif (val <= 50):
        icon = ""
    elif (val > 50):
        icon = ""
    return icon
