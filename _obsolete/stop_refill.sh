#!/bin/bash

ps aux | grep -ie "python test_outputs" | grep -v grep | awk '{print $2}' | xargs kill -SIGINT