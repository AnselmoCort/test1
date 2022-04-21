#!/usr/bin/python3.7
import hashlib
import telebot
import time
import json
import requests
import MySQLdb
import datetime
from bs4 import BeautifulSoup
from telebot import types
number='+79063886667'
key='a2cbc29d4d1a4c121b31f7fc7d5bba78'

prices={'подписчики':0.15,'приват':0.1,'подписчики инста':0.01, 'лайки инста':0.1,'подписчики2':0.25,'подписчики3':0.18}

class SQLighter:
  def __init__(self):
        self.conn = MySQLdb.connect("localhost","root","A1katra519","bot_db",charset = "utf8", use_unicode = True) #,charset='utf8'

        self.c = self.conn.cursor()
  def sel_from(self,m):
     try:
      return self.c.execute("SELECT * FROM nakrutka_bot WHERE id =(%s)"% (m))
     finally:
                 self.c.close()
                 self.conn.close()

  def insert(self,query):
        try:
            self.c.execute(query)
            self.conn.commit()
        finally:
                 self.c.close()
                 self.conn.close()
  def update(self,q,m,z):
   try:
    data = (m,z)
    self.c.execute(q,data)
    self.conn.commit()
    rows =self.c.fetchall()
    return rows
   finally:
                 self.c.close()
                 self.conn.close()
  def update2(self,q):
   try:
    #data = (i,z, m)
    self.c.execute(q)
    self.conn.commit()
    rows =self.c.fetchall()
    return rows
   finally:
                 self.c.close()
                 self.conn.close()
  def updatee24(self,q):
   try:

    self.c.execute(q)
    self.conn.commit()
    rows =self.c.fetchall()
    rows2 =self.c.description
    return rows,rows2
   finally:
                 self.c.close()
                 self.conn.close()
  def updateargs(self,q,*args):
   try:
    data = (args)
    self.c.execute(q,data)
    self.conn.commit()
    rows =self.c.fetchall()
    return rows
   finally:
                 self.c.close()
                 self.conn.close()


  def updatee24(self,q):
   try:

    self.c.execute(q)
    self.conn.commit()
    rows =self.c.fetchall()
    rows2 =self.c.description
    return rows,rows2
   finally:
                 self.c.close()
                 self.conn.close()




#query = "ALTER TABLE nakrutka_bot ADD %s VARCHAR(150)" % ('last_service')
#SQLighter().insert(query)

#SQLighter().updateargs(""" UPDATE  qiwi_last_date SET date = (%s) WHERE date != %s """,'2020-01-09T09:39:54+03:00',1)

def db_create(table_name,lis):

    createsqltable = """CREATE TABLE IF NOT EXISTS """ + table_name + " (" + " VARCHAR(1000),".join(lis) + " VARCHAR(1000))"
    SQLighter().insert(createsqltable)

db_create('nakrutka_bot',['id', 'username','date' ,'balance','last_amount','last_channel','last_price'])
db_create('qiwi_last_date',[ 'date'])
db_create('nakrutka_orders',['id', 'username','date' ,'channel','price','amount'])

def checkk(name):
        q = "SELECT * FROM  %s"%name;rows,desc=SQLighter().updatee24(q);column_names = [col[0] for col in desc];li=[];li2=[]
        for i in range(0,len(column_names)):li.append(i)
        li2=[]
        for i in range(0,len(column_names)):

             mes=str(li[i])+' '+str(column_names[i]);li2.append(mes)
             #mes=str(column_names[i]);li2.append(mes)
        print (name,li2)

def add_order(chat_id, username,channel,price,amount):
 dt = str(datetime.datetime.now().replace(microsecond=0)).split(' ')[0]
 query = "INSERT INTO nakrutka_orders (id, username,date,channel,price,amount) VALUES ('%s','%s','%s','%s','%s','%s')" % (chat_id,username,str(dt),channel,price,amount)
 SQLighter().insert(query)

checkk('nakrutka_bot');checkk('nakrutka_orders')


#query = "INSERT INTO qiwi_last_date (date) VALUES ('%s')" % ('2019-12-16T21:23:51+03:00')
#SQLighter().insert(query)

def add_usr(chat_id,usname):
 dt = datetime.datetime.now().replace(microsecond=0)
 query = "INSERT INTO nakrutka_bot (id, username,date,balance,last_amount,last_channel) VALUES ('%s','%s','%s','%s','%s','%s')" % (chat_id,usname,str(dt),0,0,0)
 SQLighter().insert(query)


api='1041126730:AAG9p0QAzFhWNi6JvyAmdMaumjj6HbCfdFI'
bot = telebot.TeleBot(api,threaded=False)
bot.stop_polling()
bot.delete_webhook()
print('working')

@bot.message_handler(content_types=['audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location','contact','new_chat_members','left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'])
def callback_inliness2(call):

        print('strange content')



@bot.message_handler(commands=['start', 'help'])
def send_welcom11e(message,):


  x=SQLighter().sel_from(message.chat.id)
  if x==0 :

      add_usr(message.chat.id,get_usrnamee(message))





  mes='''❗️ Обязательно прочтите информацию о боте.
        Если бот не отвечает жми: /start '''
  bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=get_main_menu() )


@bot.message_handler(func = lambda message:   '↪️' in message.text or 'Главное меню' in message.text or 'В главное меню' in message.text)
def back_tomainmenu(message):

  mes='Главное меню'
  bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=get_main_menu() )

def get_main_menu():
  markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
  markup.add('🚀 Продвижение в Telegram B1 🚀')
  markup.add('🎭 Продвижение в Telegram B2 🎭')
  markup.add('💰 Баланс','♻️ Мои заказы')
  markup.add('❗️ Информация',)#'💡 Автопросмотры')
  return markup


@bot.message_handler(func = lambda message:   '🎭 Продвижение в Telegram B2 🎭' in message.text )
def insta_subs(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add('👥 Подписчики RU2','👤 Подписчики BOT')
    mes='Выберите услугу'
    markup.add('↪️ В главное меню')
    bot.send_message(message.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True,reply_markup=markup)



@bot.message_handler(func = lambda message: '👤 Подписчики BOT'  in message.text)
def insta_likes(message):
    SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_service = (%s) WHERE id = %s """,'лайки',message.chat.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    mes=f'''💰Цена за 10 подписчиков - 1 руб.
                      100 подписчиков - 10 руб.
                      ...
            ❗Введите ссылку на канал: ( https://t.me/Your_Channel )  '''

    markup.add('↪️ В главное меню')
    z=bot.send_message(message.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True,reply_markup=markup)
    bot.register_next_step_handler(z, handle_instagr_likes)


def handle_instagr_likes(message):
     if 'В главное меню' in message.text or '↪️' in message.text or 'start' in message.text : back_tomainmenu(message);return
     SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_channel = (%s) WHERE id = %s """,message.text,message.chat.id)
     markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

     markup.add('↪️ В главное меню')
     mes='''🔻Введите желаемое количество подписчиков:
     мин/макс количество для заказа:
    10-20 000 '''
     z=bot.send_message(message.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True,reply_markup=markup)
     bot.register_next_step_handler(z, handle_instagr_likes2)

def handle_instagr_likes2(message):
     if 'В главное меню' in message.text or '↪️' in message.text or 'start' in message.text : back_tomainmenu(message);return
     work_with_order(message,handle_instagr_likes2,10, prices['приват'])  #500k base



@bot.message_handler(func = lambda message:   '👥 Подписчики RU2' in message.text )
def insta_subs2(message):
    if 'Подписчики' in message.text: serv='подписчики'
    else: serv='лайки'
    print(2123,serv)


    SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_service = (%s) WHERE id = %s """,serv,message.chat.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    mes=f'''💰Цена за 100 подписчиков - 18 руб
                     1000 подписчиков - 180 руб
                            ...
            ❗Введите ссылку на канал: (https://t.me/Your_Channelе)   '''

    markup.add('↪️ В главное меню')
    z=bot.send_message(message.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True,reply_markup=markup)
    bot.register_next_step_handler(z, handle_instagr_sub)

def handle_instagr_sub(message):
     if 'В главное меню' in message.text or '↪️' in message.text or 'start' in message.text : back_tomainmenu(message);return
     SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_channel = (%s) WHERE id = %s """,message.text,message.chat.id)
     markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

     markup.add('↪️ В главное меню')
     mes='''🔻Введите желаемое количество подписчиков:
               мин/макс количество для заказа:
            10-20 000 '''
     z=bot.send_message(message.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True,reply_markup=markup)
     bot.register_next_step_handler(z, handle_instagr_sub2)


def handle_instagr_sub2(message):
     if 'В главное меню' in message.text or '↪️' in message.text or 'start' in message.text : back_tomainmenu(message);return
     work_with_order(message,handle_instagr_sub2,10,prices['подписчики3'])  #cheap base





def work_with_order(message,func,minim,price):
         markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
         markup.add('↪️ В главное меню')
         mes='Введите только цифру'
         try:
            b=int(message.text)

         except:
             markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)


             z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)
             bot.register_next_step_handler(z, func);return

             return

         if float(message.text)<minim:
             mes=f'Введите правильное количество\n\nМинимальное количество для заказа {minim} '
             z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)
             bot.register_next_step_handler(z, func);return

         usr=SQLighter().update2("SELECT * FROM   nakrutka_bot WHERE id =(%s)"%message.chat.id)
         price=int(message.text)*price
         SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_amount = (%s),last_price=(%s) WHERE id = %s """,message.text,price,message.chat.id)
         if float(usr[0][3])<price:

            mes=f'💳У вас недостаточно денег на балансе. Пожалуйста пополните сначала баланс или укажите меньшее количетсво подписчиков.\n\nДоступный баланс <b>{usr[0][3]}р.</b>'
            z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)
            bot.register_next_step_handler(z, func);return

         else:
            mes=f"""
            ✅Ваш заказ:

Канал: {usr[0][5]}

Количество: <b>{message.text}</b>

Цена: <b>{price}</b>

Подтвердить заказ?

            """
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
            print(3223,usr[0][7])
            if usr[0][7]=='Telegram1':
                markup.add('▶️ Да','↪️ Нет')
            elif usr[0][7]=='Telegram2':
                    markup.add('🎯 Да','↪️ Нет')
            else:
                markup.add('💫 Да','↪️ Нет')
            z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup,disable_web_page_preview=True)

@bot.message_handler(func = lambda message:   '💫' in message.text )
def work_with_order_inst(message):
    usr=SQLighter().update2("SELECT * FROM   nakrutka_bot WHERE id =(%s)"%message.chat.id)
    if float(usr[0][3])>=float(usr[0][6]):
        SQLighter().updateargs(""" UPDATE  nakrutka_bot SET balance = balance- (%s) WHERE id = %s """,usr[0][6],message.chat.id)
        mes='Ваш заказ создан'
        bot.send_message(message.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True)


        add_order(message.chat.id, get_usrnamee(message),usr[0][5],usr[0][6],usr[0][4])

        if  usr[0][7]=='подписчики':serv='5147'
        else:serv='5134'

        bulkfollows_order(usr[0][5],usr[0][4],serv)
        back_tomainmenu(message)
    else:
        mes=f'💳У вас недостаточно денег на балансе. Пожалуйста пополните сначала баланс или укажите меньшее количетсво подписчиков.\n\nДоступный баланс <b>{usr[0][3]}р.</b>'
        bot.send_message(message.chat.id, mes,parse_mode='HTML')
        back_tomainmenu(message)

@bot.message_handler(func = lambda message:   '♻️' in message.text )
def all_orders(message):
    orders=SQLighter().update2("SELECT * FROM   nakrutka_orders WHERE id =(%s)"%message.chat.id)

    total=len(orders)
    if  total<1:
        active=0
        lstorders=' '

    else:

        dt = str(datetime.datetime.now().replace(microsecond=0)).split(' ')[0]
        print(32322323,dt)
        active=SQLighter().updateargs("SELECT * FROM   nakrutka_orders WHERE date=(%s) AND id =(%s)",dt,message.chat.id)
        active=len(active)
        lstorders=orders[-10:]
        lstorders=[f'Канал: {i[3]}\nКоличество: <b>{i[5]}</b> \nЦена: <b>{i[4]}</b>'  for i in lstorders]
        lstorders='\n\n'.join(lstorders)
    mes=f"""
♻️ Всего заказов: {total}
🚀 Активных заказов: {active}

Последние 10 заказов:\n{lstorders}"""
    bot.send_message(message.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True)



@bot.message_handler(func = lambda message:   '💰' in message.text )
def balance(message):
    usr=SQLighter().update2("SELECT * FROM   nakrutka_bot WHERE id =(%s)"%message.chat.id)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add('💲Пополнить счет')
    markup.add('↪️ В главное меню')
    bal='{0:.2f}'.format(float(usr[0][3]))
    mes=f'💲 Ваш баланс: {bal}р.🏷 \n\nВаш id: <b>{message.chat.id}</b>'
    bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)



@bot.message_handler(func = lambda message:   '💲' in message.text )
def topupbal(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add('💵 Проверить платеж')
    markup.add('↪️ В главное меню')
    bot.send_message(message.chat.id, 'Ваша ссылка для оплаты',parse_mode='HTML')#,reply_markup=keyboard)



    mes=f'🔥Для автоматического пополнения баланса переведите деньги на этот QIWI кошелек:\n\n<b>{number}</b>\nсо следующим  комментарием к переводу \n\n<b>'+str(message.chat.id)+'</b>\n\n⛔️Очень важно оставить код в комментарии, иначе платеж не будет засчитан!\n️После отправки нажмите кпопку проверить платеж сумма зачислится в течение 1 минуты'

    bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)


from dateutil.parser import parse
from dateutil import parser
@bot.message_handler(func = lambda message: '💵' in message.text)
def check_qiwi(m):





    qiwi_before=SQLighter().updateargs("SELECT * FROM   qiwi_last_date WHERE date !=(%s)",'1')
    qiwi_before=qiwi_before[0][0]; print(qiwi_before)
    #with open('QIWI.txt','r') as f:
      #       qiwi_before=f.read()

    try:
        print('Обработка')
        s = requests.Session()
        s.headers['authorization'] = 'Bearer ' + key
        parameters = {'rows': '10'}
        h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+number+'/payments', params = parameters)
        x=json.loads(h.text)
    except Exception as e:
        print(3232,e)

    try:
        for i in x['data']:
         try:
          if i['status'] == "SUCCESS":
              last_qiwi=str(x['data'][0]['date'])
              if(qiwi_before!=last_qiwi):
                  if i['comment']==None:

                          print('no comment')
                  else:
                       code = i['comment']
                       print('Inserted code:  ',code)
                  dt=parser.parse(qiwi_before)
                  dt1= i['date']
                  dt1 = parser.parse(dt1)
                  print('dates')
                  print(dt)
                  print(dt1)
                  if len(code) >0 and dt1>dt:
                                    idd=i['comment']

                                    print(00000,idd)

                                    print(123,idd)
                                    try:

                                        usr=SQLighter().updateargs("SELECT * FROM   nakrutka_bot WHERE id =(%s)",idd)
                                        if len(usr)>0:
                                            invest = float(i['sum']['amount'])
                                            print(invest)





                                            SQLighter().updateargs(" UPDATE nakrutka_bot SET balance =balance+ (%s) WHERE id = %s ",invest,idd)




                                            mes= 'Ваш платеж зачислен: ' +str(invest)
                                            try:

                                                bot.send_message(231125267, mes+f'\nid пользователя: {idd}')
                                                bot.send_message(idd, mes)
                                            except:pass




                                    except Exception as e:
                                            print(traceback.format_exc())
                                            mes=' Неизвестный код'
                                            bot.send_message(231125267,mes)


         except Exception as e :
             print(555322323,e)

        SQLighter().updateargs(" UPDATE qiwi_last_date SET date = (%s) WHERE date != %s ",last_qiwi,1)
        #with open('QIWI.txt','w') as f:
            #f.write(str(last_qiwi))
    except Exception as e:
        print(767767657,traceback.format_exc())
        print(e)
        pass



@bot.message_handler(func = lambda message:   '🚀 Продвижение в Telegram B1 🚀' in message.text )
def order_sub(message):
    mes='Выберите пункт меню'
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add('📍 Telegram1 - 👀 просмотры')
    markup.add('📍 Telegram2 - подписчики RU')
   # markup.add('📍 Telegram3 - подписчики BOT')
    markup.add('В главное меню')
    z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)

@bot.message_handler(func = lambda message:   '📍 Telegram1 - 👀 просмотры' in message.text )
def orders(message):
    typ=message.text.split(' ')[1]
    SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_service = (%s) WHERE id = %s """,typ,message.chat.id)
    mes=f"""
            💰Цена за 100 просмотров - 1 руб
                     1000 просмотров - 10 руб.
            ❗️Введите ссылку на ваш пост
              например - https://t.me/channel/2 """

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

    markup.add('В главное меню')
    z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)


    bot.register_next_step_handler(z, handle_channelname)

@bot.message_handler(func = lambda message:   '📍 Telegram2 - подписчики RU' in message.text )
def orders2(message):
    typ=message.text.split(' ')[1]
    SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_service = (%s) WHERE id = %s """,typ,message.chat.id)
    mes=f"""
            💰Цена за: 100 подписчиков - 25руб
                      1000 подписчиков - 250 руб...
            ❗Введите ссылку на канал: (https://t.me/Your_Channelе) """

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

    markup.add('В главное меню')
    z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)


    bot.register_next_step_handler(z, handle_channelname22)


def handle_channelname22(message):
    if 'В главное меню' in message.text or '↪️' in message.text or 'start' in message.text : back_tomainmenu(message);return


    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

    markup.add('В главное меню')
    if 'me' not in message.text and '@' not in message.text:

        mes='Проверьте правильность введенных даных и попробуйте снова'
        z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)
        bot.register_next_step_handler(z, handle_channelname)
        return
    elif 'join' in message.text:
        mes='Проверьте правильность введенных даных. Мы принимаем только открытые каналы'
        z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)
        bot.register_next_step_handler(z, handle_channelname)
    else:
        mes=f"""
        🎗️Вы раскручиваете канал - {message.text}

🔻Введите необходимое количество подписчиков:

 мин/макс количество для заказа:
    500-30 000
        """

        SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_channel = (%s) WHERE id = %s """,message.text,message.chat.id)

        z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup,disable_web_page_preview=True)
        usr=SQLighter().update2("SELECT * FROM   nakrutka_bot WHERE id =(%s)"%message.chat.id)

        bot.register_next_step_handler(z, handle_channelamount22)

def handle_channelamount22(message):
         if 'В главное меню' in message.text: back_tomainmenu(message);return
         work_with_order(message,handle_instagr_sub2,500,prices['подписчики2'])   #ру подписчики


@bot.message_handler(func = lambda message:   '📍 Telegram3 - подписчики BOT' in message.text )
def orders3(message):
    typ=message.text.split(' ')[1]
    SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_service = (%s) WHERE id = %s """,typ,message.chat.id)
    mes=f"""
             💰Цена за: 100 подписчиков - 12 руб.
             ❗️Введите адрес публичного канала
             например: @address
                                                """

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

    markup.add('В главное меню')
    z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)


    bot.register_next_step_handler(z, handle_channelname33)

def handle_channelname33(message):
    if 'В главное меню' in message.text or '↪️' in message.text or 'start' in message.text : back_tomainmenu(message);return


    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

    markup.add('В главное меню')
    if 'me' not in message.text and '@' not in message.text:

        mes='Проверьте правильность введенных даных и попробуйте снова'
        z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)
        bot.register_next_step_handler(z, handle_channelname)
        return
    elif 'join' in message.text:
        mes='Проверьте правильность введенных даных. Мы принимает только открытые каналы'
        z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)
        bot.register_next_step_handler(z, handle_channelname)
    else:
        mes=f"""
        🎗️Вы раскручиваете канал - {message.text}
🤖 Стоимость одного подписчика - {prices['подписчики3']}  руб.


🔻Введите необходимое количество подписчиков:

(минимальное количество для заказа 100 подписчиков)
        """

        SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_channel = (%s) WHERE id = %s """,message.text,message.chat.id)

        z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup,disable_web_page_preview=True)
        usr=SQLighter().update2("SELECT * FROM   nakrutka_bot WHERE id =(%s)"%message.chat.id)

        bot.register_next_step_handler(z, handle_channelamount33)

def handle_channelamount33(message):
         if 'В главное меню' in message.text: back_tomainmenu(message);return
         work_with_order(message,handle_instagr_sub2,100,prices['подписчики3']) # Т3

def handle_channelname(message):
    if 'В главное меню' in message.text or '↪️' in message.text or 'start' in message.text : back_tomainmenu(message);return


    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)

    markup.add('В главное меню')
    if 'me' not in message.text and '@' not in message.text:

        mes='Проверьте правильность введенных даных и попробуйте снова'
        z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)
        bot.register_next_step_handler(z, handle_channelname)
        return
    elif 'join' in message.text:
        mes='Проверьте правильность введенных даных. Мы принимает только открытые каналы'
        z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup)
        bot.register_next_step_handler(z, handle_channelname)
    else:
        mes=f"""
        🎗️Вы раскручиваете канал - {message.text}

🔻Введите необходимое количество просмотров:

 мин/макс количество для заказа:
    50-100 000
        """

        SQLighter().updateargs(""" UPDATE  nakrutka_bot SET last_channel = (%s) WHERE id = %s """,message.text,message.chat.id)

        z=bot.send_message(message.chat.id, mes,parse_mode='HTML',reply_markup=markup,disable_web_page_preview=True)
        usr=SQLighter().update2("SELECT * FROM   nakrutka_bot WHERE id =(%s)"%message.chat.id)

        bot.register_next_step_handler(z, handle_channelamount)



def create_task_panel(chan,amount,serv):

    url='https://justanotherpanel.com/api/v2'
    API='3c6548ea008810a7ede88f2a6fc6ac21'
    action='balance'
    params = {'key': '3c6548ea008810a7ede88f2a6fc6ac21', 'action': 'balance'}

    z=requests.post(url,params=params)
    print(z.text)

    params = {'key': '3c6548ea008810a7ede88f2a6fc6ac21', 'action': 'add','service':serv,'link':chan,'quantity':amount}
    z=requests.post(url,params=params)
    print(z.text)


def handle_channelamount(message):
         if 'В главное меню' in message.text: back_tomainmenu(message);return
         work_with_order(message,handle_instagr_sub2,50,prices['подписчики инста']) #просмотры

@bot.message_handler(func = lambda message:   '▶️' in message.text or '🎯' in  message.text )
def accept_channel(message):

    usr=SQLighter().update2("SELECT * FROM   nakrutka_bot WHERE id =(%s)"%message.chat.id)
    if float(usr[0][3])>=float(usr[0][6]):
        SQLighter().updateargs(""" UPDATE  nakrutka_bot SET balance = balance- (%s) WHERE id = %s """,usr[0][6],message.chat.id)
        mes='Ваш заказ создан'
        bot.send_message(message.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True)


        add_order(message.chat.id, get_usrnamee(message),usr[0][5],usr[0][6],usr[0][4])
        if '🎯' in message.text:
            create_task_panel(usr[0][5],usr[0][4],'5916')
        else:
          create_task_panel(usr[0][5],usr[0][4],'1365')
        back_tomainmenu(message)
    else:
        mes=f'💳У вас недостаточно денег на балансе. Пожалуйста пополните сначала баланс или укажите меньшее количетсво подписчиков.\n\nДоступный баланс <b>{usr[0][3]}р.</b>'
        bot.send_message(message.chat.id, mes,parse_mode='HTML')
        back_tomainmenu(message)

def bulkfollows_order(chan,amount,service_id):
    url='https://bulkfollows.com/api/v2'
    API='72047d001517fee9b2632415ca45b329'

    params = {'key': API, 'action': 'balance'}

    z=requests.post(url,params=params)
    print('BULKKK',z.text)
    z=z.json()
    print('service balance: ',z['balance'])
    if float(z['balance'])<0.1:
        mes='Баланс исчерапн, обратитесь в поддержку '
        bot.send_message(785839324,mes)


    params = {'key': API, 'action': 'add','service':service_id,'link':chan,'quantity':amount}

    z=requests.post(url,params=params)
    print(z.text)

@bot.message_handler(func = lambda message:   '❗️' in message.text )
def information(message):

    mes="""
    🔻 Главная информация:

     Просто и недорого.
     Мы предлагаем качественный и недорогой способ продвижения Вашего канала.
     Выберите необходимую вам услугу и следуйте дальнейшим инструкциям.
    _____________________________________

    🔷Telegram Base1

     Telegram1 - 👀 просмотры (база 100 тысяч)
     Лимиты до 100К просмотров на 1 канал в день.
     Быстрый старт. Просмотры приходят запасом!
     [10руб/1000шт] [50мин-200 000макс]

     Telegram RU - 👥 подписчики (база 30 тысяч)
     Большинство с никнеймами и авками,
     5-10% просматривают записи.
     Быстрый старт 0-1ч. Скорость до 3к/день.
     Качество акаунтов - REAL
     Поднимают канал в поиске!
     [250руб/1000шт] [500мин-30 000макс]
    _____________________________________

     🔶Telegram Base2

     Подписчики RU2 👥 (база 300 тысяч)
     Старт до 1ч. Скорость до 10к/день.
     [180руб/1000шт] [10мин-300 000макс]

     Подписчики BOT 👥 (база 20 тысяч)
     MIX регионы.
     До 5к/день, на один канал
     Качество акаунтов - BOT
     [100руб/1000шт] [10мин-500 000макс]
     ____________________________________

    🤝По всем вопросам @manager_cheat

      """

    keyboard = types.InlineKeyboardMarkup()
   # url_button = types.InlineKeyboardButton(text="Сайт", url="https://promotionup.ru")
    # keyboard.add(url_button)
    z=bot.send_message(message.chat.id, mes, parse_mode='HTML', reply_markup=keyboard)

@bot.message_handler(func = lambda message: 'add_balance'in message.text)
def hi23s11dwdw32(msg):

    #if msg.chat.id==231125267 or msg.chat.id==319517631:
        mes='Введите баланс и ид через пробел,например: 23123123 10'
        z=bot.send_message( msg.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True)
        bot.register_next_step_handler(z, adddbalaa)



def adddbalaa(msg):
    idd,b=msg.text.split(' ')
    query = """ UPDATE  nakrutka_bot SET balance = (%s) WHERE id = %s """
    SQLighter().update(query,b,idd)
    mes='Баланс пользователя обновлен'
    z=bot.send_message( msg.chat.id, mes,parse_mode='HTML',disable_web_page_preview=True)




def add_inline(z):
    kb = types.InlineKeyboardMarkup()
    kb.add(*[types.InlineKeyboardButton(text=name,callback_data=name)for name in z])
    return kb





def get_usrnamee(message):
        if message.from_user.username is not None: m=message.from_user.username;m='@'+m
        else:
            m=str(message.from_user.first_name)+' '+str(message.from_user.last_name)
        return m


def get_keyboard(m):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    if len (m)==1:markup.add(m[0]);return markup;
    if len(m)% 2 == 0:

        for i in range(0, len(m), 2):

                markup.add(m[i],m[i + 1] )
        return markup
    else:
        for i in range(0, len(m)-1, 2):

                markup.add( m[i],m[i + 1] )
        markup.add(m[-1])
        return markup;

import traceback
while True:
     try:
        bot.polling(none_stop=True)
     except Exception as e:
         print(traceback.format_exc())

         time.sleep(2)
