# DeerRunner 🦌

> **NOTE** This is a very *early and hacky* utility made for my personal use, as it stands it is not really usable by a general audience. Hopefully, this will change as I continue to develop and use it.

**DeerRunner** is a linux utility for automatically porting and natively running games made in certain supported engines. The goal is:

* Being able to easily run games through a simple `RunGame' command inside the game's directory
* Allow more games to be playable on arm linux
* Avoid some of the perfomance and compatibility issues that come with using Wine

## Supported Players

* **ags (Adventure Game Studio)** - adventure game engine
* **renpy** - python based visual novel engine
* **easyrpg** - rpg maker 2000
* **mkxp-z** - rpg maker xp
* **nw.js** - various engines (ie. rpg maker mv/mz)

##  Mode of operation

DeerRunner is meant to be run in the directory of the game one wants to play, when run it performs the following actions:

0. Checks if a DeerRunner `RunGame.sh` file already exists in the directory  and runs it, else:
1. **Detects** which Engine is used
2. **Builds** the files for the engine's player if none already exist
3. **Installs** any needed player files and creates a `RunGame.sh` for that game
