#!/usr/bin/python3
import install
import os
import subprocess
import sys

if len(sys.argv) == 2:
    os.chdir(os.path.join(os.getcwd(),sys.argv[1]))

if not os.path.exists("RunGame.sh"):
    engine = install.engine_detect()
    if engine:
        print(f"Detected Engine: '{engine}'")
        if engine in install.install:
            install.install[engine]()
            subprocess.run(["/usr/bin/notify-send", "--icon=dialog-information", f"Detected and installed {engine} runner!"])
    else:
        subprocess.run(["/usr/bin/notify-send", "--icon=error", "Could not detect compatible engine in folder!"])
if os.path.exists("RunGame.sh"):
    path = os.path.abspath(os.getcwd())
    subprocess.run(["sh",f"{path}/RunGame.sh"])