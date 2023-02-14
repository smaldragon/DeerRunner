# Largely based  on https://github.com/mkxp-z/mkxp-z/wiki/Compilation
cd builds

git clone https://github.com/Splendide-Imaginarius/mkxp.git #https://github.com/mkxp-z/mkxp-z
cd mkxp-z/linux

# Replace mkxp-z SDL2 repo with official SDL2 repo for improved os compatibility :smil:
sed -i -e 's|/mkxp-z/SDL $(DOWNLOADS)/sdl2 -b mkxp-z;|/libsdl-org/SDL $(DOWNLOADS)/sdl2 -b SDL2;|g' Makefile

make

# Export the variables necessary to find the stuff we built
source ./vars.sh

# Configure the build
cd ..; meson build

# Build the thing
cd build && ninja

# Feast your eyes upon your work
#xdg-open .

# Set up the build to install everything locally
meson configure --bindir=. --prefix=$PWD/local

# Do the thing
ninja install

# See the thing
#xdg-open $PWD/local

# Copy
cp -r local ../../../libs/mkxp-z