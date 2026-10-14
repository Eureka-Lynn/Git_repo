from machine import I2C, Pin, RTC
import ds1307
import time

i2c=I2C(0, scl=Pin(17), sda=Pin(16))
r=machine.RTC()

print(i2c.scan())
ds = ds1307.DS1307(i2c)
ds.halt(False)
print("ds1307: ",ds.datetime())
print("rtc:    ",r.datetime())
rs=r.datetime()

ds.datetime((rs[0], rs[1], rs[2], rs[3], rs[4], rs[5], rs[6]))
print()
print("ds1307: ",ds.datetime())
print("rtc:    ",r.datetime())
time.sleep(1)
print()
print("ds1307: ",ds.datetime())
print("rtc:    ",r.datetime())