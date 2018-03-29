#!/usr/bin/env python3
#============================================================
#========================== author ==========================
#============================================================
#
#  ██████╗ ██╗   ██╗██╗   ██╗ █████╗ ██████╗ ████████╗
#  ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██╗╚══██╔══╝
#  ██████╔╝██║   ██║██║   ██║███████║██████╔╝   ██║   
#  ██╔══██╗██║   ██║██║   ██║██╔══██║██╔══██╗   ██║   
#  ██████╔╝╚██████╔╝╚██████╔╝██║  ██║██║  ██║   ██║   
#  ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
#
# автор: Шиликов Андрей buuart@gmail.com
# ver. b0.1
#
# Файл инструкций для светомузыкальной инсталяци "7 сопок" компании Concrete Jungle
# работа определяется включением системы по наступлению темноты и работой в течение 2 часов,
# после переход в режим статичной подсведки с сохранением воспроизведения музыки.
# можно увязать с временами года, так как наступление сумерек разнится от месяца к месяцу
#
# ПЕРВЫМ ДЕЛОМ ПРОВЕРЯЙ DEFIN'Ы!!!

#============================================================
#======================= << TO DO >> ========================
#============================================================
# [ ] определение плэй листа
# [+] функция воспроизведения
# [ ] рандомайзер для воспроизведения (или случайное воспроизведение всего списка) через define
# [+] логирование событий 
# [+] привязать дропбокс или гугл диск
# [ ] рассписание окончания воспроизведения музыки? (~ с 23:30?)
# [ ] прописать методы классов
# [+] прописать defines

#============================================================
#========================= defines ==========================
#============================================================
LOGGING_NAME='7_sopok'
LOGGING_FILE_NAME='logger.log'
LIGHT_SHOW_DURATION=120 # значение в минутах
PLAYED_SONG_LOG=True #true - писать в лог файл, False - не писать
RANDOM_TRACK=False # случайный перебор треков или воспроизведение по порядку (True будет перемешивать)
MUSIC_FOLDER='D:/Desktop/testDir/Music/' # корневая папка с музыкой
VLC_START_PREFIX='start D:/VLC/vlc.exe file:///' # префикс для запуска нескольких объектов плеера
SERIAL_PORT_NAME='COM4' #имя порта проверяй, где висит контроллер
SERIAL_PORT_BAUDRATE=9600 # скорость обмена
SERIAL_PORT_TIMEOUT=1 # таймаут - оставь единицу, чтобы не завесить программу при работе с внешним железом

#============================================================
#========================== import ==========================
#============================================================
import logging
logger=logging.getLogger(LOGGING_NAME)
logger.setLevel(logging.INFO)
fh=logging.FileHandler(LOGGING_FILE_NAME)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info('logging imported')
import os
logger.info('os imported')
import time
logger.info('time imported')
import serial
logger.info('serial imported')
import random
logger.info('random imported')
from mutagen.mp3 import MP3
logger.info('mutagen imported')

#============================================================
#======================== variables =========================
#============================================================
class Amplify():
	def on(self):
		#print('Amp is on')
		logger.info('Amp->on')
		#serial.println('0')
	def off(self):
		# print('Amp is off')
		logger.info('Amp->off')
		#serial.println('0')

class Lights():
	def on(self):
		# print('Lamps is on')
		logger.info('Amp->on')
		#serial.println('0')
	def off(self):
		# print('Lamps is off')
		logger.info('Amp->off')
		#serial.println('0')

class Dim_Mode():
	def on(self):
		# print('Dim is on')
		logger.info('Amp->on')
		#serial.println('0')
	def off(self):
		# print('Dim is off')
		logger.info('Amp->off')
		#serial.println('0')

device_name=[' vlc://quit --no-video --aout=waveout --waveout-audio-device="Динамики (USB Audio Device) ($ffff,$ffff)"',' vlc://quit --no-video --aout=waveout --waveout-audio-device="Динамики (2- USB Audio Device) ($ffff,$ffff)"',' vlc://quit --no-video --aout=waveout --waveout-audio-device="Динамики (2- Realtek High Definition Audio) ($ffff,$ffff)"']
Amplify_power=0 # флаг состояния питания усилителей
Light_Mode=0 # флаг состояния режима подсветки
Light_power=0 # флаг состояния питания ламп
sleep_delay=10 # время между замерами уровня освещённости
tracklis=[] # массив будет содержать очерёдность треков
previous_light_state=0 # флаг состояния освещённости при прошлом замере 
light_show_end={'time':0,'flag':True} # настройка времени светового шоу после включения
logging.info('Programm started')

Amp=Amplify() # объекты классов
Lamps=Lights()
Dim=Dim_Mode()

#============================================================
#======================== functions =========================
#============================================================
def chk_lgt():
		pass

def play_track(track_folder):
	trackname_list=os.listdir(MUSIC_FOLDER+track_folder)
	trackname_list=trackname_list[:len(device_name)]
	max_duration=[]
	for i in range(len(trackname_list)):
		audio=MP3(MUSIC_FOLDER+track_folder+'/'+trackname_list[i])
		max_duration.append(audio.info.length)
	sleep_after=max(max_duration)+2
	for i in range(len(trackname_list)):
		os.system(VLC_START_PREFIX+MUSIC_FOLDER+track_folder+'/'+trackname_list[i]+device_name[i])
	logging.info(track_folder + ' played')
	time.sleep(sleep_after)

#============================================================
#========================== setup ===========================
#============================================================
logging.info('begin setup')
#Serial.setup произвести

Amp.off()
time.sleep(1)
Lamps.off()
time.sleep(1)
Dim.off()
time.sleep(1)
logging.info('setup done')
logging.info('light_show_duration'+str(LIGHT_SHOW_DURATION))

#============================================================
#========================= routine ==========================
#============================================================

while():
	if(chk_lgt()):
		if(Amplify_power=1):
			Amp.off()
			Amplify_power=0
			time.sleep(1)
		if(Light_Mode=1):
			Dim.off()
			Light_Mode=0
			time.sleep(1)
		if(Light_power=1)
			Lamps.off()
			Light_power=0
			time.sleep(1)
		light_show_end['flag']=False
		time.sleep(sleep_delay)
		if (previous_light_state==0):
			logging.info('morning')
			previous_light_state=1
	else:
		if(previous_light_state==1):
			logging.info('evening')
			previous_light_state=0
		if(Amplify_power=0):
			Amp.on()
			Amplify_power=1
		time.sleep(2)
		if(Light_power=0):
			Lamps.on()
			Light_power=1
		time.sleep(2)
		if (light_show_end['flag']==False):
			light_show_end['flag']=True
			light_show_end['time']=int(time.time())+(LIGHT_SHOW_DURATION*60)
		if(light_show_end['time']<=time.time()):
			if(Light_Mode=0):
				Dim.on()
				Light_Mode=1
				logging.info('Dim Mode on')
		else:
			if(Light_Mode=1):
				Dim.off()
				Light_Mode=0
				logging.info('Dim Mode off')
		
		# if(time.localtime().tm_hour==22 and (time.localtime().tm_minute>2 or time.localtime().tm_minute<30):
		# 	light_show_end['flag']=False
		#if tracklist exist - play(trackname)
		#+ delay


