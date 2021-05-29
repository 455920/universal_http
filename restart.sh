#!/bin/bash

ps aux | grep 'python3 run.py'| grep -v 'grep' | awk '{print $2}' | xargs kill -9

nohup python3 run.py&