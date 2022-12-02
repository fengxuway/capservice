#!/bin/bash

docker build -t myimage .

docker run -d -p 8000:8000 -v ${PWD}/db/:/src/db/ -v ${PWD}/static/files/:/src/static/files/ myimage
