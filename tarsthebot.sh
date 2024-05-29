#!/bin/sh

PATH=/usr/bin

# Verifica se a sessão existe antes de tentar encerrá-la
if tmux has-session -t tarsthebot 2>/dev/null; then
    tmux kill-session -t tarsthebot
fi

# Cria uma nova sessão
cd /home/abdiasviana/Repositories/botInfoRPi
source env/bin/activate
tmux new -s tarsthebot -d python3 bot_info_rasp.py
