import time

import telebot
from telebot import types

TOKEN = '1904661680:AAH1PUPGGyL1BLzXQa1JX91euhvGduODSjk'

knownUsers = [] 
userStep = {} 

commands = {

    'start'       : '▶️\nIniciar bot\n\n',
    
    'help'        : '🆘\nMuestra todos los comandos disponibles\n\n',
    
    'consultas'   : '🔍\nMuestra un teclado personalizado donde usted puede gestionar diferentes opciones'
}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
imageSelect.add('Formula cuadratica', 'Formula conversion de unidades', 'Documento Historia de Ucrish', 'Ubicacion de Ucrish')

hideBoard = types.ReplyKeyboardRemove()  
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("He detectado a un nuevo usuario mas sin envargo no ha usado el comando \"/start\"")
        return 0



def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:
        knownUsers.append(cid)
        userStep[cid] = 0
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "¡Hola!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Es un gusto ayudarte")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Puedes realizar las siguientes consultas")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Formula cuadratica \nFormula conversion de unidades \nDocumento Historia de UCRISH \nUbicacion de UCRISH")
        command_help(m)
    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ya usaste el comando /start, usa otro comando, por favor")


@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    bot.send_chat_action(cid, 'typing')
    time.sleep(3)
    help_text = "Por favor, elije un comando o escríbelo\n\n\nEstos son los comandos que estan disponibles:\n\n\n"
    bot.send_chat_action(cid, 'typing')
    time.sleep(5)
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text) 



@bot.message_handler(commands=['consultas'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Selecciona una opcion:", reply_markup=imageSelect) 
    userStep[cid] = 1 



@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text

    bot.send_chat_action(cid, 'typing')

    if text == 'Formula cuadratica': 
        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es la: \nFormula cuadratica")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('Formula cuadratica.png', 'rb'), 
        reply_markup=hideBoard)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /consultas para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "🧐")
        userStep[cid] = 0  
    elif text == 'Formula conversion de unidades':
        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es la: \nFormula conversion de unidades")
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)
        bot.send_photo(cid, open('conversion.jpg', 'rb'), 
        reply_markup=hideBoard)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /consultas para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "🧐")
        userStep[cid] = 0  

    elif text == 'Documento Historia de Ucrish':
        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es la: \n Historia de Ucrish")
        bot.send_chat_action(cid, 'upload_document')
        time.sleep(3)
        bot.send_document(cid, open('Historia Ucrish.pdf', 'rb'), 
        reply_markup=hideBoard)
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /consultas para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "🧐")
        userStep[cid] = 0  

    elif text == 'Ubicacion de Ucrish':
        bot.send_chat_action(cid, 'typing')
        time.sleep(3) 
        bot.send_message(cid, "Esta es la: \nUbicacion de Ucrish")
        bot.send_chat_action(cid, 'find_location')
        time.sleep(5)
        bot.send_location(cid, 15.495411328649043, -87.99132672470155) 
        
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Espero haberte ayudado, usa el comando /consultas para realizar otra consulta")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Ó bien puedes usar el comando /start para reiniciar el bot.")
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        bot.send_message(cid, "¡Saludos!")
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.send_message(cid, "🧐")
        userStep[cid] = 0  
    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Por favor usa el teclado predefinido")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "Vamos, intentalo de nuevo, sólo selecciona una opción")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_message(cid, "👍")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    bot.send_message(m.chat.id, "No entiendo la palabra \"" + m.text + "\"\n Usa el comando /start para reiniciar el bot, el comando /paises si necesitas realizar una consulta sobre algún país ó puedes usar el comando /help si necesitas ayuda.")


bot.infinity_polling()
