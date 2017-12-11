import os
import time
# code to create beep
""" beep sourced from https://stackoverflow.com/questions/6537481/python-making-a-beep-noise """ 
beep = lambda x: os.system("echo TIME IS UP '\a';sleep 0.2;" * x)

def countdown(n):
    while n > 0:
        n = n -1
        time.sleep(1)
        if n ==0:
            beep(1)

countdown(5)