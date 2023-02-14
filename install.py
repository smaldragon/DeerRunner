#!/usr/bin/python3
import os
import stat
import shutil
import subprocess

def engine_detect():
    if os.path.isdir("renpy"):
        return "renpy"
    if os.path.isfile("Game.ini"):
        return "mkxp-z"
    if os.path.isfile("package.json"):
        return "nw.js"
    if os.path.isfile("RPG_RT.exe"):
        return "easyrpg"
    return None

def renpy_install():
    libpath = os.path.dirname(os.path.abspath(__file__))
    
    with open("RunGame.sh","w") as f:
        f.write(f"{libpath}/libs/renpy/renpy.sh .")
    os.chmod("RunGame.sh",0o711)

def mkxpz_build():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    subprocess.run(["sh",f"mkxpz-build.sh"])

def mkxpz_install():
    libpath = os.path.dirname(os.path.abspath(__file__))
    
    if not os.path.isdir(f"{libpath}/libs/mkxp-z"):
        cwd = os.getcwd()
        mkxpz_build()
        os.chdir(cwd)

    for f in os.listdir(f"{libpath}/libs/mkxp-z/"):
        if f.startswith("lib"):
            shutil.copytree(os.path.join(f"{libpath}/libs/mkxp-z/",f),f)
        if f.startswith("mkxp-z"):
            shutil.copy(os.path.join(f"{libpath}/libs/mkxp-z/",f),"mkxp-z")

    with open("RunGame.sh","w") as f:
        f.write(f"./mkxp-z")
    os.chmod("RunGame.sh",0o711)

def easyrpg_build():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    subprocess.run(["sh",f"easyrpg-build.sh"])
    
def easyrpg_install():
    libpath = os.path.dirname(os.path.abspath(__file__))
    
    if not os.path.isdir(f"{libpath}/libs/easyrpg"):
        cwd = os.getcwd()
        easyrpg_build()
        os.chdir(cwd)
        
    with open("RunGame.sh","w") as f:
        f.write(f"{libpath}/libs/easyrpg/easyrpg-player .")
    os.chmod("RunGame.sh",0o711)

def nwjs_install():
    libpath = os.path.dirname(os.path.abspath(__file__))
    
    with open("RunGame.sh","w") as f:
        f.write(f"{libpath}/libs/nwjs/nw .")
    os.chmod("RunGame.sh",0o711)


install = {
    "renpy": renpy_install,
    "mkxp-z": mkxpz_install,
    "nw.js": nwjs_install,
    "easyrpg": easyrpg_install,
}