# How to test locally

## Pack

$ cd /path/to/src/FOOBAR
$ rm -f autograder.zip
$ zip -r autograder.zip *

## Build

$ cd /path/to/sandbox
$ mv ../src/FOOBAR/autograder.zip .
$ docker build -t autograder .

## Test

$ cd /path/to/sandbox
$ docker run --rm -it -v $(pwd):/autograder/submission autograder /bin/bash

(docker)# /autograder/run_autograder
(docker)# cat /autograder/results/results.json
