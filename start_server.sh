#! /bin/bash

python genconfig.py 
cp out.cfg ~/.openarena/baseoa/temp.cfg
openarena-server +set dedicated 2 +exec test.cfg