# -*- coding: UTF-8 -*-
from fbchat.models import *
from fbchat import log, Client
from tu_vi import TuVi
from lunarcalendar import Converter, Solar, Lunar
import random
import time
import requests
from datetime import datetime  
import pytz  

IST = pytz.timezone('Asia/Ho_Chi_Minh')  

other_text = '🙂 Xin Chào. Tôi là Bot chat của Trong Duc - Voccer. \n- Hiện tại anh ấy không thể rep tin nhắn ngay được. \n- Nếu xem tử vi gõ /tuvi <tuổi>; ví dụ: /tuvi sửu. \n-Nếu xem cung hoàng đạo gõ /hoangdao <cung>; \n ví dụ: /hoangdao song ngư\n- xem lịch gõ /lich'

class VoccerBot(Client):
    # def __init__(self):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        sleep = random.randint(3, 5)
        if author_id != self.uid:
            if message_object.text:
                if message_object.text == '/Getid' or message_object.text == '/getid':
                    self.send(Message(text=message_object.author), thread_id=thread_id, thread_type=thread_type)

                elif '/tuvi' in message_object.text:
                    tuoi = message_object.text[message_object.text.index('/tuvi') + len('/tuvi'):]
                    tuvi = TuVi()
                    loi_phan = tuvi.con_giap(Cgiap=tuoi)
                    self.send(Message(text=loi_phan), thread_id=thread_id, thread_type=thread_type)
                elif '/hoangdao' in message_object.text:
                    cung = message_object.text[message_object.text.index('/hoangdao') + len('/hoangdao'):]
                    tuvi = TuVi()
                    loi_phan = tuvi.cung_hoang_dao(cung_hd=cung)
                    # print('loi phan cua toi la {}'.format(loi_phan))
                    self.send(Message(text=loi_phan), thread_id=thread_id, thread_type=thread_type)
                elif '/lich' in message_object.text:
                    time.sleep(sleep)
                    solar_today = datetime.now(IST)
                    lunar_today = Converter.Solar2Lunar(Solar(solar_today.year, solar_today.month, solar_today.day))
                    self.send(Message(
                        text="Hôm nay, \nDương lịch: {}-{}-{}\nÂm lịch: {}-{}-{}".format(solar_today.day, solar_today.month, solar_today.year,lunar_today.day, lunar_today.month, lunar_today.year)),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )
                else:
                    time.sleep(sleep)
                    self.send(Message(text=other_text),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )
            else:
                time.sleep(sleep)
                self.send(Message(text=other_text),
                        thread_id=thread_id,
                        thread_type=thread_type
                    )

            #check birthay
            info = self.get_birthday()
            if info:
                congrate = 'Hôm nay là sinh nhật của: \n' 
                for i in info:
                    congrate += 'Tên: ' + i[1] + '\n'
                    congrate += 'Tuổi: ' + str(i[0]) + '\n'
                    congrate += 'Loại: ' + 'âm lịch' if i[2] == 'solar' else 'dương lịch'

                     
                self.send(Message(text=congrate),
                        thread_id='100009594708355',
                        thread_type=ThreadType.USER
                    )
    
    def get_birthday(self):
        r = requests.get('https://docs.google.com/document/u/0/export?format=txt&id=1b2aQMfZvhLhqs5bnGrdNZUnOSmCGsuNZeSH8Qk6ndrg&token=AC4w5VjlljBzAvNU8CtCSnvvFwe52p-2-w%3A1589941528767&ouid=102939292131381354747&includes_info_params=true&inspectorResult=%7B%22pc%22%3A1%2C%22lplc%22%3A20%7D')
        b = r.text.split('\n')

        solar_today = datetime.now(IST)
        lunar_today = Converter.Solar2Lunar(Solar(solar_today.year, solar_today.month, solar_today.day))
        
        info = []
    
        for i in b:
            if i == '':
                continue
            name_birthday = i.split(':')[0]
            solar_birthday = i.split(':')[1].replace(' ', '')
            solar_day = int(solar_birthday.split('/')[0]) 
            solar_month = int(solar_birthday.split('/')[1])
            solar_year = int(solar_birthday.split('/')[2])

            # exception unknown
            if solar_day == 0:
                solar_day = 1
            if solar_month == 0:
                solar_month = 1    
            if solar_year == 0:
                solar_year = 1900
            
            try:
                lunar_birthday = Converter.Solar2Lunar(Solar(solar_year, solar_month, solar_day))
            except Exception as e:
                print(e)
                print(solar_year, solar_month, solar_day)

            if solar_day == solar_today.day and solar_month == solar_today.month:
                age = str(solar_today.year - solar_year)
                info.append([age, name_birthday, 'solar'])
            if lunar_birthday.day == lunar_today.day and lunar_birthday.month == lunar_today.month:
                age = str(lunar_today.year - lunar_birthday.year)
                info.append([age, name_birthday, 'lunar'])
        
        return info


