import subprocess
import time
def open_pulse():
    uri = "C:/Program Files (x86)/Common Files/Pulse Secure/JamUI/Pulse.exe"
    process = subprocess.Popen(uri, subprocess.PIPE)
    time.sleep(2)

    if process== 0:
        return True
    else:
        return False
