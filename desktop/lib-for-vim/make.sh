#!/bin/bash
sudo rm /usr/lib/libvimlib.so
gcc -w -shared -o libvimlib.so -fPIC main.c -lrt
sudo ln ./libvimlib.so /usr/lib/libvimlib.so
