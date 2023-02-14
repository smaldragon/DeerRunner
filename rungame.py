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
        print("Could not detect compatible engine")
if os.path.exists("RunGame.sh"):
    path = os.path.abspath(os.getcwd())
    subprocess.run(["sh",f"{path}/RunGame.sh"])