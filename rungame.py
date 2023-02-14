#!/usr/bin/python3
import install
import os
import subprocess

if not os.path.exists("RunGame.sh"):
    engine = install.engine_detect()
    if engine:
        print(f"Detected Engine: '{engine}'")

        if engine in install.install:
            install.install[engine]()
            print("Successfully Installed Engine Files!")
    else:
        subprocess.run(["/usr/bin/notify-send", "--icon=error", "Could not detect compatible engine in folder!"])
if os.path.exists("RunGame.sh"):
    path = os.path.abspath(os.getcwd())
    subprocess.run(["sh",f"{path}/RunGame.sh"])