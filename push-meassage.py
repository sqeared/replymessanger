# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:27:39 2022

@author: omina
"""
from linebot import LineBotApi
from linebot.models import TextSendMessage
import time


line_bot_api = LineBotApi('BotMZmLEcw0LfOe3ONBpCTcq+BlHcOD8zxzVz5tETYfKR4HCJW8y60bzCp3+7G4aT21Y1GICgmvPpdPsaEFVeXH4AvWTob8rPdBFnkKJgDed6uHVTVNZ6S7/FXl5SO82V+rA9YdS8fMI66T/OIc5rAdB04t89/1O/w1cDnyilFU=')

yourID = 'Ue5a33ec4d43958a17917c57eecfc088f'

line_bot_api.push_message(yourID, 
                          TextSendMessage(text='Hello Sir, Have you eaten your breakfast?'))

for i in [1,2,3,4,5]:
    line_bot_api.push_message(yourID, 
                              TextSendMessage(text='lets count down：'+str(i)))
    time.sleep(1)
