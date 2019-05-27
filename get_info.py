from __future__ import print_function
from weather import Weather, Unit
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

def get_services_info():
    oCatolicoBotService = subprocess.getoutput('systemctl status botinforpi.service \n')
    eachService = '--------------------------------- \n'
    botInfoRpi = subprocess.getoutput('systemctl status ocatolicobot.service \n ')

    return botInfoRpi, eachService, oCatolicoBotService