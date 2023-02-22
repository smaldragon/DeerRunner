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
    if os.path.isfile("acsetup.cfg"):
        return "ags"
    return None

def sf2_install(dest):
    libpath = os.path.dirname(os.path.abspath(__file__))
    src = f"{libpath}/libs/soundfont.sf2"
    print("uh",src)
    if not os.path.isfile(src):
        print("downlading soundfont...")
        cwd = os.getcwd()
        os.chdir(f"{libpath}/libs")
        
        SF2_8MBGM = "https://github.com/exeex/mimi/raw/master/mimi/soundfont/8MBGMSFX.SF2"
        SF2_FLUID = "https://github.com/Jacalz/fluid-soundfont/raw/master/original-files/FluidR3_GM.sf2"
        SF2_MERLIN = "https://github.com/wrightflyer/SF2_SoundFonts/raw/master/merlin_gmv32.sf2"
        subprocess.run([
            "wget",
            SF2_MERLIN,
            "-Osoundfont.sf2"
        ])
        
        os.chdir(cwd)
    os.symlink(src,dest)

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
    
    sf2_install("easyrpg.soundfont")
    
    with open("RunGame.sh","w") as f:
        f.write(f"{libpath}/libs/easyrpg/easyrpg-player .")
    os.chmod("RunGame.sh",0o711)

def nwjs_install():
    libpath = os.path.dirname(os.path.abspath(__file__))
    
    with open("RunGame.sh","w") as f:
        f.write(f"{libpath}/libs/nwjs/nw .")
    os.chmod("RunGame.sh",0o711)

def ags_build():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    subprocess.run(["sh",f"ags-build.sh"])

def ags_install():
    libpath = os.path.dirname(os.path.abspath(__file__))
    
    if not os.path.isdir(f"{libpath}/libs/ags"):
        cwd = os.getcwd()
        ags_build()
        os.chdir(cwd)
    
    game_exe = None
    for f in os.listdir("."):
        if f.endswith(".exe") and f != "winsetup.exe":
            game_exe = f
            break
    
    if game_exe:
        with open("RunGame.sh","w") as f:
            f.write(f"{libpath}/libs/ags/ags \"{game_exe}\"")
        os.chmod("RunGame.sh",0o711)

install = {
    "renpy": renpy_install,
    "mkxp-z": mkxpz_install,
    "nw.js": nwjs_install,
    "easyrpg": easyrpg_install,
    "ags": ags_install,
}