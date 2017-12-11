# author: @shannonmcdermitt

import time
def countdown(n):
    while n > 0:
        print(n)
        #time.sleep(sec) function will countdown
        time.sleep(1)
        n = n -1
        if n ==0:
            print('blast off')
countdown(60)

"""
is there a way to print this in a separate window
so time can be observed as decreasing by the user?
"""