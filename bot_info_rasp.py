import telebot
from get_info import * 

token = '685098141:AAGEtCbrHfeixKRs5WreVTo6xYX4hvODqJg'
bot = telebot.TeleBot(token)

oCatolicoBotService = subprocess.getoutput('systemctl status botinforpi.service')
botInfoRpi = subprocess.getoutput('systemctl status ocatolicobot.service')
old_ip = get_ip()

@bot.message_handler(commands = ['info', 'start'])
def send_info(message):
    old_ip = get_ip()
    now = get_time()
    bot.send_message(message.chat.id, 'Hi Sir {}'.format(message.chat.username))
    bot.send_message(message.chat.id, 'System Time: {}/{}/{} - {}:{}:{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second))
    bot.send_message(message.chat.id, 'IP Ext: {}'.format(str(old_ip)))
    bot.send_message(message.chat.id, "CPU Temp: {:.1f}'C".format(get_cpu_temp()))
    bot.send_message(message.chat.id, 'GPU Temp: {}'.format(get_gpu_temp()))

    bot.send_message(message.chat.id, '-----------------------------------------------')
    bot.send_message(message.chat.id, oCatolicoBotService)
    bot.send_message(message.chat.id, '-----------------------------------------------')
    bot.send_message(message.chat.id, botInfoRpi)

while old_ip != get_ip():
        send_info()    

bot.polling()
