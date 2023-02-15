cd builds
git clone https://github.com/adventuregamestudio/ags.git
cd ags

make --directory=Engine

# Copy files
mkdir ../../libs/ags
cp Engine/ags ../../libs/ags/ags