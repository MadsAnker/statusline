#!/usr/bin/env python3
from statusline.statusline import getStatusLine
import subprocess

subprocess.run(["xsetroot", "-name", "{}".format(getStatusLine())])

