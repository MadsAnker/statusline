import subprocess
import re

def getWifiStatus():
    response = subprocess.run("nmcli", capture_output=True, encoding='utf-8')
    match = re.search("(?<!dis)connected to ([\w]*)", response.stdout)
    if match:
        return " {}".format(match.group(1))
    else:
        return ""
