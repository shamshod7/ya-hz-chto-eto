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

def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode=None):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)   
    
client1=os.environ['database']
client=MongoClient(client1)
db=client.chlenomer
idgroup=db.ids
iduser=db.ids_people
penis=db.penis

ban=[667532060]

wait=[]
ch=[]
members=[]
play=[]


msgcount=0
pods4et=0


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
writed=[
]
massive=['Хер','хер','Член','член','Хуй','хуй']
elita=[]

@bot.message_handler(commands=['combine'])
def combine(m):
    if m.from_user.id==441399484:
        try:
            x1=int(m.text.split(' ')[1])
            x2=int(m.text.split(' ')[2])
            iduser.update_one({'id':x2},{'$inc':{'summ':iduser.find_one({'id':x1})['summ']}})
            iduser.update_one({'id':x2},{'$inc':{'kolvo':iduser.find_one({'id':x1})['kolvo']}})
            bot.send_message(x2, 'Перенёс данные со старого аккаунта на новый!')
            bot.send_message(441399484, 'gotovo')
        except:
            bot.send_message(441399484, traceback.format_exc())


@bot.message_handler(commands=['add'])
def adddsfdgeh(m):
    if m.from_user.id==441399484:
        try:
            id=int(m.text.split(' ')[1])
            iduser.update_one({'id':id},{'$inc':{'chlenocoins':int(m.text.split(' ')[2])}})
            bot.send_message(m.chat.id, 'Членокоины добавлены!')
        except:
            bot.send_message(441399484, traceback.format_exc())
            
                                             
            
            
@bot.message_handler(commands=['update'])
def upddd(m):
    if m.from_user.id==441399484:
        iduser.update_many({}, {'$set':{'msgcount':0, 'penisincs':0}})
        bot.send_message(m.chat.id, 'updated')

@bot.message_handler(commands=['count'])
def counttt(m):
    if m.from_user.id==441399484:
        global pods4et
        pods4et=1
        t=threading.Timer(60, ends4et, args=[m.chat.id])
        t.start()
        bot.send_message(m.chat.id, 'Считаю количество сообщений за минуту.')
        
def ends4et(id):
    global msgcount
    global pods4et
    bot.send_message(id, 'Количество сообщений за минуту: '+str(msgcount)+'.')
    msgcount=0
    pods4et=0
    
    
@bot.message_handler(commands=['mafia'])
def mafia(m):
    if m.from_user.id not in ban:
        incmsg(m.from_user.id, m.chat.id, m.message_id)
        try:
            pass
            #bot.send_message(m.from_user.id, '@mafiacw')
        except:
            pass
           # bot.send_message(m.chat.id, 'Ссылку на чат я отправляю только в личку (не все чаты любят посторонние ссылки). Начните со мной диалог, чтобы я мог это сделать.')
    
    

@bot.message_handler(commands=['globalchlen'])
def globalpeniss(m):
    if m.from_user.id not in ban:
        incmsg(m.from_user.id, m.chat.id, m.message_id)
        penis.update_one({},{'$inc':{'penis':0.1}})
        iduser.update_one({'id':m.from_user.id},{'$inc':{'penisincs':0.1}})
        p=penis.find_one({})
        ps=p['penis']
        bot.send_message(m.chat.id, 'Вы увеличили мой член на 0.1 см! Текущая длина: '+str(round(ps,2))+' см!')
        
@bot.message_handler(commands=['id'])
def iddd(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    if m.reply_to_message!=None:
        user=m.reply_to_message.from_user
        bot.send_message(m.chat.id, 'id выбранного пользователя:\n'+'`'+str(user.id)+'`',reply_to_message_id=m.message_id,parse_mode='markdown')
    else:
        bot.send_message(m.chat.id, 'Чтобы узнать id пользователя, введите эту команду, ответив на его сообщение.')

@bot.message_handler(commands=['chatid'])
def chatid(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    bot.send_message(m.chat.id, 'Айди чата: `'+str(m.chat.id)+'`', parse_mode='markdown')
    
    
        
@bot.message_handler(commands=['donate'])
def donatemes(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    bot.send_message(m.chat.id, 'Если вам нравится бот и вы хотите поддержать разработчика, переводите деньги на карту:\n`5336 6900 5562 4037`\nЗаранее благодарю)', parse_mode='markdown')

@bot.message_handler(commands=['removedailyuser'])
def removedailyu(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    pass
    x=bot.get_chat_member(m.chat.id, m.from_user.id)
    if 'administrator' in x.status or 'creator' in x.status or m.from_user.id==441399484:
            chat=idgroup.find_one({'id':m.chat.id})
            try:
                if len(m.text.split(' '))==2:
                    user=chat['topdaily'][m.text.split(' ')[1]]
                    if user['id']!=441399484:
                        idgroup.update_one({'id':chat['id']},{'$set':{'topdaily.'+str(user['id']):{'name':user['name']}}})
                        bot.send_message(m.chat.id, 'Юзер был успешно удалён из списка!')
                    else:
                        bot.send_message(m.chat.id, 'Вы не можете удалить администратора бота из списка!')
                else:
                    bot.send_message(m.chat.id, 'Чтобы удалить юзера из ежедневного розыгрыша, введите эту команду в таком формате:\n'+
                                     '/removedailyuser *USERID*, где *USERID* - айди участника, которого вы хотите удалить. Взять его можно '+
                                     'по команде /id.\n\nВНИМАНИЕ!!!\nУдалив участника из списка, вы сбросите его чатовую статистику ежедневных '+
                                     'розыгрышей!',parse_mode='markdown')
            except:
                bot.send_message(m.chat.id, 'Юзер с таким id не регистрировался в этом чате!')
               
    else:
        bot.send_message(m.chat.id, 'Вы не админ чата!')
    
    
    
@bot.message_handler(commands=['sendm'])
def sendmes(message):
    if message.from_user.id==441399484:
        x=idgroup.find({})
        y=iduser.find({})
        tex=message.text.split('/sendm')
        usend=0
        gsend=0
        for one in x:
            try:
              bot.send_message(one['id'], tex[1])
              gsend+=1
            except:
                pass
        for one in y:
            try:
              bot.send_message(one['id'], tex[1])
              usend+=1
            except:
                pass
        bot.send_message(441399484, 'Отправлено сообщений юзерам: '+str(usend)+'\n'+
                         'Отправлено сообщений группам: '+str(gsend))
        
        
        
@bot.message_handler(commands=['sendp'])
def sendmesssss(message):
    if message.from_user.id==441399484:
        y=iduser.find({})
        tex=message.text.split('/sendm')
        usend=0
        for one in y:
            try:
              bot.send_message(one['id'], tex[1])
              usend+=1
            except:
                pass
        bot.send_message(441399484, 'Отправлено сообщений юзерам: '+str(usend))


@bot.message_handler(commands=['elita']) 
def elit(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    if m.from_user.id in elita:
        Kb = types.ReplyKeyboardMarkup()
        Kb.add(types.KeyboardButton("Член"))
        Kb.add(types.KeyboardButton("Хер"))
        bot.send_message(m.from_user.id, 'Вы элита!', reply_markup=Kb)
    
    
#@bot.message_handler(commands=['update'])
#def upd(m):
#  if m.from_user.id==441399484:
#         try:
#            idgroup.update_many({}, {'$set':{
#                                            
#                                             
#          
#                                            }
#                                    }
#                                )
 #           print('yes')
    #     except:
      #      pass
            
@bot.message_handler(commands=['stoyak'])
def biggest(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    if m.from_user.id!=m.chat.id:
        x=idgroup.find_one({'id':m.chat.id})
        if x!=None:
          if x['dailyroll']==1:
            nmb=0
            for zz in x['topdaily']:
              nmb+=1
            if nmb>0:
              x['dailyroll']=0
              idgroup.update_one({'id':m.chat.id},{'$set':{'dailyroll':0}})
              bot.send_message(m.chat.id, 'Начинаю поиск по базе данных...')
              t=threading.Timer(2, turn2, args=[m.chat.id])
              t.start()
            else:
              bot.send_message(m.chat.id, 'Нет ни одного зарегистрированного пользователя! Нажмите /dailychlenreg для того, '+
                             'чтобы я добавил вас в список.')
          else:
            bot.send_message(m.chat.id, 'Сегодня уже был проведён розыгрыш! Со стояком был замечен:\n\n'+x['todaywinner']+'!')
        else:
            bot.send_message(m.chat.id, 'Сначала напишите в группу что-нибудь!')
        
def turn2(id):
    bot.send_message(id, 'Сканирую каждый член, не двигайтесь...')
    t=threading.Timer(2, turn3, args=[id])
    t.start()
    
    
def turn3(id):
    x=idgroup.find_one({'id':id})
    lst=[]
    for ids in x['topdaily']:
        try:
            lst.append(x['topdaily'][ids]['id'])
        except:
            pass
    if len(lst)>0:
        y=random.choice(lst)
        name=x['topdaily'][str(y)]['name']
        try:
            username=x['topdaily'][str(y)]['username']
            if username==None:
                username='None'
        except:
            username='None'
        idgroup.update_one({'id':id},{'$inc':{'topdaily.'+str(y)+'.dailywins':1}})
        idgroup.update_one({'id':id},{'$inc':{'topdaily.'+str(y)+'.currentwinstreak':1}})
        x=idgroup.find_one({'id':id})
        if x['topdaily'][str(y)]['maxwinstreak']<x['topdaily'][str(y)]['currentwinstreak']:
            idgroup.update_one({'id':id},{'$set':{'topdaily.'+str(y)+'.maxwinstreak':x['topdaily'][str(y)]['currentwinstreak']}})
        idgroup.update_one({'id':id},{'$set':{'todaywinner':name}})
        for ids in x['topdaily']:
          try:
            if x['topdaily'][ids]['id']!=y:
                idgroup.update_one({'id':id},{'$set':{'topdaily.'+str(x['topdaily'][ids]['id'])+'.currentwinstreak':0}})
          except:
            pass
        bot.send_message(id, 'Измерения успешно проведены. В данный момент стояк можно наблюдать у пользователя:\n\n'+name+' (@'+username+')!')
    else:
        bot.send_message(id, 'В этой группе на ежедневный розыгрыш не зарегистрировано ни одного пользователя!')

    
    
@bot.message_handler(commands=['topchlens'])
def topchlen(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    x=idgroup.find_one({'id':m.chat.id})
    if x!=None:
        text=''
        z=1
        winlist=[]
        while z<11:
            winid=0
            maxnumber=-1
            da=0
            for ids in x['topdaily']:
                try:
                    if x['topdaily'][ids]['dailywins']>maxnumber and x['topdaily'][ids]['id'] not in winlist:
                        da=1
                        winid=x['topdaily'][ids]['id']
                        maxnumber=x['topdaily'][ids]['dailywins']
                except:
                    pass
            if da==1:
                winlist.append(winid)
                text+=str(z)+'. '+x['topdaily'][str(winid)]['name']+': '+str(x['topdaily'][str(winid)]['dailywins'])+'\n'
            z+=1
        if text=='':
            text='В этой группе не было проведено ни одного розыгрыша!'
        bot.send_message(m.chat.id, 'Топ-10 пользователей, чей член больше всего раз был замечен в стоячем состоянии:\n\n'+text)

        bot.send_message(441399484, 'Топ-10 пользователей, чей член больше всего раз был замечен в стоячем состоянии:\n\n'+text)

                
                
                        
                       
    
@bot.message_handler(commands=['dailychlenreg'])
def dailyr(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    if m.from_user.id!=m.chat.id:
        x=idgroup.find_one({'id':m.chat.id})
        if x!=None:
         p=0
         for ids in x['topdaily']:
            try:
                if x['topdaily'][ids]['id']==m.from_user.id:
                    p=1
            except:
                pass
         if p==0:
            idgroup.update_one({'id':m.chat.id},{'$set':{'topdaily.'+str(m.from_user.id):createdailyuser(m.from_user.id, m.from_user.first_name,m.from_user.username)}})
            bot.send_message(m.chat.id, 'Вы успешно зарегистрировались!')
         else:
            bot.send_message(m.chat.id, 'Ты уже в игре!')
        else:
            bot.send_message(m.chat.id, "Сначала напишите в чат что-нибудь!")
    else:
        bot.send_message(m.chat.id, 'Можно регистрироваться только в группах!')


@bot.message_handler(commands=['usecoins'])
def usecoins(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    bot.send_message(m.chat.id, '@petwarbot - тут можно подраться своим питомцем')
    
    
@bot.message_handler(commands=['mysize'])
def size(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    x=iduser.find_one({'id':m.from_user.id})
    try:
        sredn=x['summ']/x['kolvo']
        sredn=round(sredn, 2)
    except:
        sredn=0
    try:
        bot.send_message(m.chat.id, m.from_user.first_name+', средний размер вашего члена: '+str(sredn)+' см.\nВы измеряли член '+str(x['kolvo'])+' раз(а)!') 
        bot.send_message(441399484, m.from_user.first_name+', средний размер вашего члена: '+str(sredn)+' см.\nВы измеряли член '+str(x['kolvo'])+' раз(а)!')
    except:
        bot.send_message(m.chat.id, 'Измерьте член хотя бы 1 раз!')
                        
    
    
@bot.message_handler(commands=['me'])
def mme(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    x=iduser.find_one({'id': m.from_user.id})
    try:
     bot.send_message(m.chat.id, m.from_user.first_name+', Ваши членокоины: '+str(x['chlenocoins'])+'. За 5 вы можете купить питомца! (Команда /buypet).')
     bot.send_message(441399484, m.from_user.first_name+', Ваши членокоины: '+str(x['chlenocoins'])+'. Сейчас они не нужны, но следите за обновлениями - в будущем они понадобятся!')                                                                                                                                     
    except:
        bot.send_message(m.chat.id, 'Упс! Какая-то ошибка! Наверное, вы ни разу не измеряли член! (напишите боту "член")')
        bot.send_message(441399484, 'Упс! Какая-то ошибка! Наверное, вы ни рару не измеряли член!')                                                                                                                               
                                                                 

                
@bot.message_handler(commands=['channel'])
def channel(message):
  if message.from_user.id not in ban:
    incmsg(message.from_user.id, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Канал обновлений: @chlenomer')
                     

@bot.message_handler(commands=['start'])
def startms(message):
  if message.from_user.id not in ban:
    incmsg(message.from_user.id, message.chat.id, message.message_id)
    if message.from_user.id==message.chat.id:
      bot.send_message(message.from_user.id, 'Если ты здесь, то ты наверняка хочешь измерить член! Пиши /commands, чтобы узнать, на какие слова реагирует бот')


@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.id==441399484:
        group=0
        people=0
        x=idgroup.find({})
        for element in x:
            group+=1
        y=iduser.find({})
        for element in y:
            people+=1
        bot.send_message(message.from_user.id, 'Группы: '+str(group)+'\n'+'Люди: '+str(people))
        


   
@bot.message_handler(commands=['ti_ctochlen'])
def ticto(message):
  if message.from_user.id not in ban:
    incmsg(message.from_user.id, message.chat.id, message.message_id)
    bot.send_message(message.from_user.id, 'Умеет менять размер члинуса')
                     
        
@bot.message_handler(commands=['name'])
def name(m):
  if m.from_user.id not in ban:
    incmsg(m.from_user.id, m.chat.id, m.message_id)
    player=iduser.find_one({'id':m.from_user.id})
    if player!=None:
        x=m.text.split('/name ')
        if len(x)==2:
            if len(x[1])<=40:
                try:
                    iduser.update_one({'id':m.from_user.id}, {'$set':{'pet.name':x[1]}})
                    bot.send_message(m.from_user.id, 'Вы успешно переименовали питомца!')
                except:
                    bot.send_message(m.from_user.id, 'У вас нет питомца!')          
            else:
                bot.send_message(m.from_user.id, 'Длина имени не должна превышать 40 символов!')
        else:
            bot.send_message(m.from_user.id, 'Неверный формат! Пишите в таком формате:\n'+'/name *имя*, где *имя* - имя вашего питомца.', parse_mode='markdown')
    else:
        bot.send_message(m.from_user.id, 'Сначала напишите боту "член" хотя бы один раз!')
         

@bot.message_handler(commands=['dick'])
def dd(m):
    global number
    text='"💎Cheksizlik Toshi" qaysi qutiga yashirilgan? .'
    kb=types.InlineKeyboardMarkup(3)
    buttons1=[]
    buttons2=[]
    buttons3=[]
    amount=random.randint(1,8)
    i=0
    dicks=[]
    golddicks=[]
    while i<amount:
        x=random.randint(1,8)
        while x in dicks:
            x=random.randint(1,8)
        dicks.append(x)
        i+=1
    i=1
    while i<=9:
        randoms=random.randint(1,10000000)
        if i in dicks:
            if random.randint(1,3)!=1:
                callb='penis'
            else:
                callb='goldpenis'
                golddicks.append(i)
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
    kb.add(types.InlineKeyboardButton(text='O`yinni tugatish', callback_data='endgame '+str(number)))
    polls.update({number:{
        'users':{},
        'dicks':dicks,
        'kb':kb,
        'golddicks':golddicks
        
    }}
                )
    bot.send_message(m.chat.id, text, reply_markup=kb)
    number+=1
    
    

@bot.callback_query_handler(func=lambda call:True)
def inline(call):
  try:
    user=call.from_user
    try:
        game=polls[int(call.data.split(' ')[1])]
    except:
        game=None
    if game!=None:
        if user.id not in game['users'] and call.data!='xyi':
            golddick=False
            if 'penis' in call.data:
                dick=True
                if 'gold' in call.data:
                    golddick=True
                    text='💎|G`alaba! Siz "Makon Toshi"ni topdingiz!'
                else:
                    text='🎴|G`alaba! Siz "Casino bileti"ni topdingiz!'
                bot.answer_callback_query(call.id, text, show_alert=True)
            else:
                dick=False
                bot.answer_callback_query(call.id, '🌀|Oo yo`q! Siz bo`m bo`sh qutini tanladiz!', show_alert=True)
            
            game['users'].update({user.id:{'name':call.from_user.first_name,
                                          'dick':dick,
                                          'golddick':golddick}})
            kb=types.InlineKeyboardMarkup(3)
            
            medit(editmsg(game), call.message.chat.id, call.message.message_id, reply_markup=game['kb'])
        
        elif 'endgame' not in call.data:
            bot.answer_callback_query(call.id, 'Siz tanlab bo`lidiz!')
        
    if 'endgame' in call.data:
        kb2=types.InlineKeyboardMarkup()
        buttons1=[]
        buttons2=[]
        buttons3=[]
        i=1
        while i<=9:
            if i in game['dicks']:
                emoj='🎴'
                if i in game['golddicks']:
                    emoj='💎'
            else:
                emoj='🌀'
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
        result=editmsg(game, True)
        medit('O`yin '+call.from_user.first_name+' tomonidan to`xtatildi! 📊Natijalar:\n'+result, call.message.chat.id, call.message.message_id, reply_markup=kb2)

  except Exception as e:
    bot.send_message(441399484, traceback.format_exc())
    
def editmsg(game, end=False):
    if end==False:
        text='Qaysi qutida "💎Makon Toshi".\n\n'
    else:
        text=''
    for ids in game['users']:
        if game['users'][ids]['golddick']==True:
            text+=game['users'][ids]['name']+': 💎"Makon Toshi"ni topdi!\n'
        
        elif game['users'][ids]['dick']==True:
            text+=game['users'][ids]['name']+': 🎴"Casino bileti"ni topdi\n'
        else:
            text+=game['users'][ids]['name']+': 💨bo`m bo`sh qutini tanladi\n'
    return text
    
    
    
print('7777')
bot.polling(none_stop=True,timeout=600)

