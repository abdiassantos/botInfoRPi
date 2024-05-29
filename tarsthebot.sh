#!/bin/sh

PATH=/usr/bin

# Verifica se a sessão existe antes de tentar encerrá-la
if tmux has-session -t tarsthebot 2>/dev/null; then
    tmux kill-session -t tarsthebot
fi

# Cria uma nova sessão
tmux new -s tarsthebot -d python3 /home/abdiasviana/Repositories/botInfoRPi/bot_info_rasp.py
