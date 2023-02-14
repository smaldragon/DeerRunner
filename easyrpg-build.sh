cd builds
git clone https://github.com/EasyRPG/Player.git -b 0-7-0-stable easyrpg
cd easyrpg
autoreconf -i
./configure
make
# Copy files
mkdir ../../libs/easyrpg
cp easyrpg-player ../../libs/easyrpg/easyrpg-player