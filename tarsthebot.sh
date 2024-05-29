#!/bin/sh

PATH=/usr/bin

tmux kill-session -t tarsthebot

tmux new -s tarsthebot -d python3 /home/abdiasviana/Repositories/botInfoRPi/bot_info_rasp.py
