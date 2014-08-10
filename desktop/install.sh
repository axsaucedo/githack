#!/bin/bash
echo Copy files
cp ./githack /usr/bin/githack
cp ./githack-init /usr/bin/githack-init

echo Build lib
gcc -w -shared -o libvimlib.so -fPIC main.c -lrt
cp ./libvimlib.so /usr/lib/libvimlib.so

cat .vimrc >> ~/.vimrc

echo "Please enter githack login:"
read userlogin
echo "Please enter githack password:"
read -s userpassword
echo user=$userlogin>/etc/githack.conf
echo password=$userpassword>>/etc/githack.conf

