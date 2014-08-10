#!/bin/bash
set -e
if [ "$(expr substr $(uname -s) 1 5)" != "Linux" ]; then
    echo "Only linux support(("
    exit 1
fi

echo Build lib
gcc -w -shared -o libvimlib.so -fPIC main.c -lrt

echo Copy files
cp ./githack /usr/bin/githack
cp ./githack-init /usr/bin/githack-init
cp ./libvimlib.so /usr/lib/libvimlib.so

cat .vimrc >> ~/.vimrc

echo "Please enter githack login:"
read userlogin
echo "Please enter githack password:"
read -s userpassword
echo user=$userlogin>/etc/githack.conf
echo password=$userpassword>>/etc/githack.conf

