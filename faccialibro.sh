#!/bin/bash
if [ -n "$1" ]; then
    if [ "$1" = "setAlbum" ]; then
        python $HOME/.faccialibro/setAlbum.py;
    else
        python $HOME/.faccialibro/faccialibro.py "$1"
    fi
else
    python $HOME/.faccialibro/faccialibro.py none
fi
