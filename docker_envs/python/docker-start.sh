#! /bin/bash

docker run -v `pwd`/executables:/executables -it python:3 python3 /executables/hello_world.py