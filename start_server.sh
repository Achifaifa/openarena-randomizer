#! /bin/bash

python genconfig.py 
mv out.cfg ~/.openarena/baseoa/temp.cfg
openarena-server +set dedicated 2 +exec temp.cfg