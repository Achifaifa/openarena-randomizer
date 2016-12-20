Openarena server cfg randomizer

* Install `openarena-server`
* run `start_server.sh`. You'll be asked if you want to randomize certain game settings and some other things.
* The server will be automatically started with the generated configuration.

To create another cfg file, you can either kill the server and run `start_server.sh` again, or generate a cfg file with `genconfig.py` and move it to `~/.openarena/baseoa/<name>.cfg`, then use `exec <name>.cfg` in the server.