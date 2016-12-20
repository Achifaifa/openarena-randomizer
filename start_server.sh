#! /bin/bash

python genconfig.py 
mv out.cfg ~/.openarena/baseoa/temp.cfg
openarena-server +set dedicated 1 +exec temp.cfg