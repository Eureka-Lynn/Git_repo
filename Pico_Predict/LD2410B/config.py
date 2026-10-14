import machine
import time
uart = machine.UART(0, baudrate=256000, tx=machine.Pin(0), rx=machine.Pin(1))
uart.write(b'\xfd\xfc\xfb\xfa\x04\x00\xff\x00\x01\x00\x04\x03\x02\x01')
time.sleep(5)
print(uart.read())
time.sleep(0.1)
uart.write(b'\xfd\xfc\xfb\xfa\x02\x00\xa3\x00\x04\x03\x02\x01')
time.sleep(0.1)
uart.read()