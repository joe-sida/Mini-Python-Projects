#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Modules
from tkinter import *
import datetime
import time
import winsound
from threading import *


# In[2]:


#Create a function that gets the actual time
def actual_time():
    set_alarm_time=f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_time)


# In[3]:


#Another function to get the Alarm time
def alarm():
    #SET ALARM AND WAITED FOR 1 SEC, THEN READ THE CURRENT TIME AND CHECK IS SET ALARM TIME AND CURRENT TIME IS EQUAL.
    #FINALLY, IF EQUAL, PLAY THE SOUND.
    
    while True:
        set_alarm=f"{hour.get()}:{min.get()}:{sec.get()}"         
        time.sleep(1)
        current_time=datetime.datetime.now().srtftime("%H:%M:%S")
        if current_time == set_alarm:
            print("WAKE UP, NIGGA")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)


# #### some GUI code goes here. Refer to this link for the FULL GUI code. Link > shorturl.at/qvKNR

# In[ ]:




