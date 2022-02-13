import telebot
import os
import subprocess
from get_info import * 

token = '1205570285:AAFBtpCDmmpB3Qnto-DTePLgA9voMmPBGI0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['info', 'start'])
def send_info(message):
        old_ip = get_ip()
        now = get_time()
        bot.send_message(message.chat.id, 'Hi Sir {}'.format(message.chat.username))
        bot.send_message(message.chat.id, 'System Time: {}/{}/{} - {}:{}:{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
        
        if message.chat.id == 48443118:
                bot.send_message(message.chat.id, 'IP Ext: {}'.format(str(old_ip)))
        # bot.send_message(message.chat.id, "CPU Temp: {:.1f}'C".format(get_cpu_temp()))
        # bot.send_message(message.chat.id, 'GPU Temp: {}'.format(get_gpu_temp()))

@bot.message_handler(commands = ['reboot'])
def send_reboot_command(message):
        if message.chat.id == 48443118:
                bot.send_message(message.chat.id, 'CASE Reiniciado')
                reboot_rasp()
        else:
                bot.send.message(message.chat.id, 'Você não possui permissão para realizar esta ação')

# Minecraft Server Commands
@bot.message_handler(commands = ['start_minecraft_server'])
def send_minecraft_start_server_command(message):
        bot.send_message(message.chat.id, 'Bom jogo xD')
        start_minecraft_server()

@bot.message_handler(commands = ['stop_minecraft_server'])
def send_minecraft_stop_server_command(message):
        bot.send_message(message.chat.id, 'Obrigado por jogar nosso servidor de Minecraft =D')
        stop_minecraft_server()
        
# Terraria Server Commands
@bot.message_handler(commands = ['start_terraria_server'])
def send_terraria_start_server_command(message):
        bot.send_message(message.chat.id, 'Bom jogo xD')
        start_terraria_server()

@bot.message_handler(commands = ['stop_terraria_server'])
def send_terraria_stop_server_command(message):
        bot.send_message(message.chat.id, 'Obrigado por jogar nosso servidor de Terraria =D')
        stop_terraria_server()

# Unturned Server Commands
@bot.message_handler(commands = ['start_unturned_server'])
def send_unturned_start_server_command(message):
        bot.send_message(message.chat.id, 'Bom jogo xD')
        bot.send_message(message.chat.id, 'Lembrando que a senha é: Arrombado')
        start_unturned_server()

@bot.message_handler(commands = ['stop_unturned_server'])
def send_unturned_stop_server_command(message):
        bot.send_message(message.chat.id, 'Obrigado por jogar nosso servidor de Unturned =D')
        stop_unturned_server()
        
bot.polling()
