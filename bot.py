# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

polls={}
number=0

try:
    pass

except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    bot.send_message(441399484, traceback.format_exc())

@bot.message_handler(commands=['dick'])
def dd(m):
    global number
    text='Угадайте, в какой коробке хуй.'
    kb=types.InlineKeyboardMarkup(3)
    buttons1=[]
    buttons2=[]
    buttons3=[]
    amount=random.randint(1,9)
    i=0
    dicks=[]
    while i<amount:
        x=random.randint(1,9)
        while x in dicks:
            x=random.randint(1,9)
        dicks.append(x)
        i+=1
    i=1
    while i<=9:
        randoms=random.randint(1,1000)
        if i in dicks:
            callb='penis'
        else:
            callb=str(random.randint(1,100))
        if i<=3:
            buttons1.append(types.InlineKeyboardButton(text='📦', callback_data=callb+' '+str(number)+' '+str(randoms)))
        elif i<=6:
            buttons2.append(types.InlineKeyboardButton(text='📦', callback_data=callb+' '+str(number)+' '+str(randoms)))
        elif i<=9:
            buttons3.append(types.InlineKeyboardButton(text='📦', callback_data=callb+' '+str(number)+' '+str(randoms)))
        i+=1
    kb.add(*buttons1)
    kb.add(*buttons2)
    kb.add(*buttons3)
    kb.add(types.InlineKeyboardButton(text='Окончить игру', callback_data='endgame'))
    polls.update({number:{
        'users':{},
        'dicks':dicks,
        'kb':kb
        
    }}
                )
    bot.send_message(m.chat.id, text, reply_markup=kb)
    number+=1
    
    

@bot.callback_query_handler(func=lambda call:True)
def inline(call):
  try:
    user=call.from_user
    game=polls[call.data.split(' ')[1]]
    if user.id not in game['users'] and call.data!='xyi':
        if 'penis' in call.data:
            dick=True
            bot.answer_callback_query(call.id, '🍆|Ура! Вы выбрали ящик с членом!', show_alert=True)
        else:
            dick=False
            bot.answer_callback_query(call.id, '💨|О нет! Вы выбрали ящик без члена!', show_alert=True)
        
        game['users'].update({user.id:{'name':call.from_user.first_name,
                                      'dick':dick}})
        kb=types.InlineKeyboardMarkup(3)
        
        medit(editmsg(game), call.message.chat.id, call.message.message_id, reply_markup=game['kb'])
        
    elif 'endgame' in call.data:
        kb2=types.InlineKeyboardMarkup()
        buttons1=[]
        buttons2=[]
        buttons3=[]
        i=1
        while i<=9:
            if i in game['dicks']:
                emoj='🍆'
            else:
                emoj='💨'
            if i<=3:
                buttons1.append(types.InlineKeyboardButton(text=emoj, callback_data='xyi'))
            elif i<=6:
                buttons2.append(types.InlineKeyboardButton(text=emoj, callback_data='xyi'))
            elif i<=9:
                buttons3.append(types.InlineKeyboardButton(text=emoj, callback_data='xyi'))
            i+=1
        kb2.add(*buttons1)
        kb2.add(*buttons2)
        kb2.add(*buttons3)
        result=editmsg(game)
        medit('Игра окончена юзером '+call.from_user.first_name+'! Результаты:\n'+result, call.message.chat.id, call.message.message_id, reply_markup=kb2)
    else:
        bot.answer_callback_query(call.id, 'Вы уже походили!')
  except Exception as e:
    bot.send_message(441399484, traceback.format_exc())
    
def editmsg(game):
    text=''
    for ids in game['users']:
        if game['users']['dick']==True:
            text+=game['users']['name']+': 🍆нашёл член\n'
        else:
            text+=game['users']['name']+': 💨открыл пустую коробку\n'
    return text
    
    
    
print('7777')
bot.polling(none_stop=True,timeout=600)

