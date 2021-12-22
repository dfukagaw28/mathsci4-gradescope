FROM gradescope/auto-builds:latest

RUN apt-get update \
    && apt-get install -y curl unzip dos2unix \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
 
RUN mkdir -p /autograder/source

RUN mkdir -p /autograder/results

RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN python3 -m pip install 'gradescope-utils>=0.3.1'

ADD autograder.zip /tmp/autograder.zip

RUN unzip -n -d /autograder/source /tmp/autograder.zip

RUN cp /autograder/source/run_autograder /autograder/run_autograder

RUN dos2unix /autograder/run_autograder /autograder/source/setup.sh

RUN chmod +x /autograder/run_autograder

RUN python3 -m pip install pandas

#RUN apt-get update \
#    && bash /autograder/source/setup.sh \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
