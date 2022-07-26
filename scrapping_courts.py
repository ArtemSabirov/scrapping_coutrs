#! / usr / bin / env python3


import pandas as pd
import requests
import re
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


headers = {'user-agent': '_____________________________________________________________'}

############################### СОБИРАЕМ ИНФОРМАЦИЮ ПО КАЖДОМУ СУДУ ИЗ СПИСКА ################################

#N-ский районный суд
response = requests.get("https://огромная в 8 строк ссылка на конкретную поисковую выдачу N-ского районного суда", headers=headers)
response.encoding = 'windows-1251'
pattern = re.compile(r'Всего по запросу найдено.....')
c = pattern.findall(response.text)
err = 0
try:
    print('N-ский районный суд', datetime.date.today(), c[0][27:]) #индекс переменной c для каждого сайта подбирал руками. Помните? Только request-хардкор! 
except IndexError:
    try:
        print('N-ский районный суд', datetime.date.today(), c[0][27:]) # распечатка нужна для отладки и просмотра работы при запуске в терминале
    except IndexError:
        err = 1
        
#N2-ский районный суд
response2 = requests.get("https://огромная в 8 строк ссылка на конкретную поисковую выдачу N2-ского районного суда", headers=headers)
response2.encoding = 'windows-1251'
pattern2 = re.compile(r'Всего по запросу найдено.....')
c2 = pattern2.findall(response2.text)
err2 = 0
try:
    print('N2-ский районный суд', datetime.date.today(), c2[0][27:])
except IndexError:
    try:
        print('N2-ский районный суд', datetime.date.today(), c2[0][27:]) 
    except IndexError:
        err2 = 1

#N3-ский районный суд
response3 = requests.get("https://огромная в 8 строк ссылка на конкретную поисковую выдачу N3-ского районного суда", headers=headers)
response3.encoding = 'windows-1251'
pattern3 = re.compile(r'Всего по запросу найдено.....')
c3 = pattern3.findall(response3.text)
err3 = 0
try:
    print('N3-ский районный суд', datetime.date.today(), c3[0][27:])
except IndexError:
    try:
        print('N3-ский районный суд', datetime.date.today(), c3[0][27:]) 
    except IndexError:
        err3 = 1
        
        
#N4-ский районный суд
response4 = requests.get("https://огромная в 8 строк ссылка на конкретную поисковую выдачу N4-ского районного суда", headers=headers)
response4.encoding = 'windows-1251'
pattern4 = re.compile(r'Всего по запросу найдено.....')
c4 = pattern4.findall(response4.text)
err4 = 0
try:
    print('N4-ский районный суд', datetime.date.today(), c4[0][27:]) 
except IndexError:
    try:
        print('N4-ский районный суд', datetime.date.today(), c4[0][27:])
    except IndexError:
        err4 = 1

#N5-ский районный суд, в котором исков к доверителю нет.
response5 = requests.get("https://огромная в 8 строк ссылка на конкретную поисковую выдачу N5-ского районного суда", headers=headers),
                          headers=headers)
pattern5 = re.compile(r'ничего не найдено')
c5 = pattern5.findall(response5.text)
err5 = 0
if c5 == ['ничего не найдено']:
    print("N5-ский районный суд ", datetime.date.today(), 0)
else:
    try:
        print("N5-ский районный суд ", datetime.date.today(), c5[0][27])
    except IndexError:
        try:
            print("N5-ский районный суд ", datetime.date.today(), c5[0][27])
        except IndexError:
            err5 = 1


###############################ГОТОВИМ ДАННЫЕ ДЛЯ ЗАПИСИ В ФАЙЛ, ЗАПИСЫВАЕМ ################################

#
# # переменные для названия файлов текущей датой
date = datetime.date.today()
filename_today = str(datetime.date.today()) + str('.txt')
filename_yesterday = str(datetime.date.today()-datetime.timedelta(days=1)) + str('.txt')
filename_2_days_ago = str(datetime.date.today()-datetime.timedelta(days=2)) + str('.txt')

# переменные для записи данных о судах с обработкой исключения "сайт капризничает"

#N-ский районный суд
if err == 1:   #на случай, если сайт не прогрузился или упал.
    N-sk = str('N-ский районный суд ') + str(date) + ' ' + str(0.1) # указываем десятичную дробь, чтобы при сравнении датасетов было видно, что информация с сайта не получена
else:
    N-sk = str('N-ский районный суд ') + str(date) + ' ' + str(c[0][27:])

#N2-ский районный суд
if err2 == 1:   
    N2-sk = str('N2-ский районный суд ') + str(date) + ' ' + str(0.1)
    N2-sk = str('N2-ский районный суд ') + str(date) + ' ' + str(c2[0][27:])

#N3-ский районный суд
if err3 == 1:   
    N3-sk = str('N3-ский районный суд ') + str(date) + ' ' + str(0.1)
    N3-sk = str('N3-ский районный суд ') + str(date) + ' ' + str(c3[0][27:])

#N4-ский районный суд
if err4 == 1:   
    N4-sk = str('N4-ский районный суд ') + str(date) + ' ' + str(0.1)
    N4-sk = str('N4-ский районный суд ') + str(date) + ' ' + str(c4[0][27:])

#N5-ский районный суд
if c5 == ['ничего не найдено']:
    N5-sk = str('N5-ский ') + str(date) + ' ' + str(0)
elif err5 == 1:
    N5-sk = str('N5-ский ') + str(date) + ' ' + str(0.1)
else:
    N5-sk = str('N5-ский ') + str(date) + ' ' + str(c5[0][2]

with open(filename_today, 'w') as f:
    f.writelines([N-sk, '\n', N2-sk, '\n', N3-sk, '\n', N4-sk, '\n', N5-sk])


###############################ФОРМИРУЕМ ДАТАСЕТЫ, СРАВНИВАЕМ, ПОЛУЧАЕМ И ПРЕОБРАЗУЕМ ИТОГОВЫЙ ДАТАСЕТ################################
x = pd.read_csv(filename_today, sep=" ", header=None)
y = pd.read_csv(filename_yesterday, sep=" ", header=None)
z = pd.read_csv(filename_2_days_ago, sep=" ", header=None)

col1 = x[2]
col2 = y[2]
col3 = z[2]

consolidated_table = z.join(col2, rsuffix='Вчера').join(col1)
consolidated_table.rename(columns={0: 'Название суда', 1: 'Дата', '2': 'Позавчера', 2: 'Сегодня'}, inplace=True)

consolidated_table['Сравнение'] =  (consolidated_table['Сегодня'] == consolidated_table['Позавчера']) & (consolidated_table['Сегодня'] == consolidated_table['2Вчера'])
html_table = consolidated_table.to_html()

###############################ОТПРАВЛЯЕМ РЕЗУЛЬТАТ СРАВНЕНИЯ ПО ПОЧТЕ################################

msg = MIMEMultipart()

message = 'Report'

# определяем параметры сообщения
password = ""
msg['From'] = ""
msg['To'] = ""
msg['Subject'] = "Report"

# добавляем текст сообщения
html_table = MIMEText(html_table, 'html')
msg.attach(html_table)

# создаем сервер
server = smtplib.SMTP('smtp.______: 587')

server.starttls()

# логинимся для отправки
server.login(msg['From'], password)

# отправляем
server.send_message(msg)

server.quit()

print("Отправлено: %s:" % (msg['To']))
