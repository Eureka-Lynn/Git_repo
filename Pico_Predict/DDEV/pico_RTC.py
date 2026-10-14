from machine import I2C, Pin, RTC
from ds1307 import DS1307
import time

i2c = I2C(0,scl=Pin(17),sda=Pin(16))
rtc = DS1307(i2c)
rtc_time = rtc.datetime()
ts = time.time()
rtc_time = list(rtc_time)
del(rtc_time[3])


print('ds1307:')

print(rtc_time) #之后要处理这个点：rtc和time模块的八元组格式不一样
'''
time:year.month.day.hour,min,second,workday,今年第几天
ds:year,month,day,workday,hour,min,second,亚秒
'''

print('system_rtc')
print(time.gmtime(ts))

print(ts)
print(time.mktime(rtc_time))