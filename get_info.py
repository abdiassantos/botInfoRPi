from __future__ import print_function
#from weather import Weather, Unit
import re
import json
from urllib.request import urlopen
import requests
import urllib
import subprocess
import psutil
import os
from datetime import datetime

def get_ip():
    url = 'http://ipinfo.io/json'
    #response = urlopen(url)
    #data = json.load(response)
    data = requests.get(url).json()

    IP=data['ip']
    org=data['org']
    city=data['city']
    country=data['country']
    region=data['region']

    return IP

def get_cpu_temp():
    tempFile = open('/sys/class/thermal/thermal_zone0/temp')
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp) / 1000
    #Mostra temperatura em Farenheit
    #return float(1.8 * gpu_temp) + 32

def get_gpu_temp():
    gpu_temp = subprocess.getoutput('/opt/vc/bin/vcgencmd measure_temp').replace('temp=', '').replace('(', '')
    return gpu_temp
    #Mostrar temperatura em Farenheit
    #return float(1.8 * gpu_temp) + 32

def get_time():
    now = datetime.now()
    return now
    # return now.month, now.day, now.year, now.minute, now.second

def reboot_rasp():
    os.system('sudo reboot')

# Minecraft Server Commands
def start_minecraft_server():
    os.system('cd /home/abdiasviana/Repositories/minecraft && source env/bin/activate && tmux new -s minecraft -d java -jar server.jar nogui')
    

def stop_minecraft_server():
    os.system('tmux kill-session -t minecraft')
    
# Terraria Server Commands
def start_terraria_server():
    os.system('cd /mnt/617b0d06-82ea-4e50-a0c3-3a2634b264c7/Terraria && tmux new -s terraria -d mono TerrariaServer.exe  -config serverconfig')
    

def stop_terraria_server():
    os.system('tmux kill-session -t terraria')
    
# Unturned Server Commands
def start_unturned_server():
    os.system('cd /mnt/617b0d06-82ea-4e50-a0c3-3a2634b264c7/Unturned/U3DS && tmux new -s unturned -d ./ServerHelper.sh +LanServer/BrodisTHE')
    

def stop_unturned_server():
    os.system('tmux kill-session -t unturned')
