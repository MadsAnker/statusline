import subprocess
import re

def getExpressVpnStatus():
    try:
        response = subprocess.run(["expressvpn", "status"], capture_output=True, encoding="utf-8")
        text = re.search("(Connected|Not connected).*", response.stdout)
        text = text.group(0)
        icon = ""
        return " {} {} ".format(icon, text)
    except:
        return ""
