#!/bin/bash
set -e

echo "Please enter githack login:"
read userlogin
echo "Please enter githack password:"
read -s userpassword
echo user=$userlogin>/etc/githack.conf
echo password=$userpassword>>/etc/githack.conf

echo
echo "Installing Githack..."

echo "Copy files"
cp ./githack /usr/bin/githack
cp ./githack-init /usr/bin/githack-init


echo
echo "Creating libraries for Vim"

opersys=$(uname -s)
opersys=${opersys:0:5}
if [ opersys != "Linux" ]; then
    echo "Only linux support for vim plugin - Time will not be taken into account."

    echo vimsupport=0>>/etc/githack.conf
    exit 1
else
  echo Building library
  gcc -w -shared -o libvimlib.so -fPIC main.c -lrt

  cp ./libvimlib.so /usr/lib/libvimlib.so
  cat vimrc >> ~/.vimrc

  echo vimsupport=1>>/etc/githack.conf
fi

echo GitHack has been installed successfully - enjoy!
