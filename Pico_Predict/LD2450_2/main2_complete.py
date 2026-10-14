from machine import UART,PWM,Pin
import time

uart = UART(0, baudrate=256000, tx=0, rx=1)
led = PWM(Pin(11,Pin.OUT))
led.freq(1000)
led_duty = 0
def r(x,y):
    return (x ** 2 + y ** 2) ** 0.5

while True:
    data = uart.read()
    if data:
        data = data[0:30]
        data_in_frame = data[4:28]
        # 目标数据切片
        target_1_data = data_in_frame[0:8]
        target_2_data = data_in_frame[8:16]
        target_3_data = data_in_frame[16:24]

        # 分别对独立对象属性切片
        target_1_x = target_1_data[0:2]
        target_1_y = target_1_data[2:4]
        target_1_speed = target_1_data[4:6]
        target_1_Range_Resolution = target_1_data[6:8]

        target_2_x = target_2_data[0:2]
        target_2_y = target_2_data[2:4]
        target_2_speed = target_2_data[4:6]
        target_2_Range_Resolution = target_2_data[6:8]

        target_3_x = target_3_data[0:2]
        target_3_y = target_3_data[2:4]
        target_3_speed = target_3_data[4:6]
        target_3_Range_Resolution = target_3_data[6:8]

        # 小端转换
        target_1_x_num = int.from_bytes(target_1_x,'little')
        target_1_y_num = int.from_bytes(target_1_y,'little')
        target_1_speed_num = int.from_bytes(target_1_speed,'little')
        target_1_Range_Resolution_num = int.from_bytes(target_1_Range_Resolution,'little')

        target_2_x_num = int.from_bytes(target_2_x,'little')
        target_2_y_num = int.from_bytes(target_2_y,'little')
        target_2_speed_num = int.from_bytes(target_2_speed,'little')
        target_2_Range_Resolution_num = int.from_bytes(target_2_Range_Resolution,'little')

        target_3_x_num = int.from_bytes(target_3_x,'little')
        target_3_y_num = int.from_bytes(target_3_y,'little')
        target_3_speed_num = int.from_bytes(target_3_speed,'little')
        target_3_Range_Resolution_num = int.from_bytes(target_3_Range_Resolution,'little')

        # 正负判断
        target_1_x_bin = bin(target_1_x_num)
        target_1_y_bin = bin(target_1_y_num)
        target_1_speed_bin = bin(target_1_speed_num)

        target_1_y_distance = '0'
        target_2_y_distance = '0'
        target_3_y_distance = '0'

        if len(target_1_x_bin) != 18:
            target_1_x_distance = - target_1_x_num
        else:
            if target_1_x_num > 32768:
                target_1_x_distance = target_1_x_num - 32768
            else:
                target_1_x_distance = target_1_x_num

        if len(target_1_y_bin) != 18:
            target_1_y_distance = - target_1_y_num
        else:
            if target_1_y_num > 32768:
                target_1_y_distance = target_1_y_num - 32768
            else:
                target_1_y_distance = target_1_y_num

        if len(target_1_speed_bin) != 18:
            target_1_speed_distance = - target_1_speed_num
        else:
            if target_1_speed_num > 32768:
                target_1_speed_distance = target_1_speed_num - 32768
            else:
                target_1_speed_distance = target_1_speed_num

        target_2_x_bin = bin(target_2_x_num)
        target_2_y_bin = bin(target_2_y_num)
        target_2_speed_bin = bin(target_2_speed_num)

        if len(target_2_x_bin) != 18:
            target_2_x_distance = - target_2_x_num
        else:
            if target_2_x_num > 32768:
                target_2_x_distance = target_2_x_num - 32768
            else:
                target_2_x_distance = target_2_x_num

        if len(target_2_y_bin) != 18:
            target_2_y_distance = - target_2_y_num
        else:
            if target_2_y_num > 32768:
                target_2_y_distance = target_2_y_num - 32768
            else:
                target_2_y_distance = target_2_y_num

        if len(target_2_speed_bin) != 18:
            target_2_speed_distance = - target_2_speed_num
        else:
            if target_2_speed_num > 32768:
                target_2_speed_distance = target_2_speed_num - 32768
            else:
                target_2_speed_distance = target_2_speed_num

        target_3_x_bin = bin(target_3_x_num)
        target_3_y_bin = bin(target_3_y_num)
        target_3_speed_bin = bin(target_3_speed_num)

        if len(target_3_x_bin) != 18:
            target_3_x_distance = - target_3_x_num
        else:
            if target_3_x_num > 32768:
                target_3_x_distance = target_3_x_num - 32768
            else:
                target_3_x_distance = target_3_x_num

        if len(target_3_y_bin) != 18:
            target_3_y_distance = - target_3_y_num
        else:
            if target_3_y_num > 32768:
                target_3_y_distance = target_3_y_num - 32768
            else:
                target_3_y_distance = target_3_y_num

        if len(target_3_speed_bin) != 18:
            target_3_speed_distance = - target_3_speed_num
        else:
            if target_3_speed_num > 32768:
                target_3_speed_distance = target_3_speed_num - 32768
            else:
                target_3_speed_distance = target_3_speed_num

        if target_1_data == b'\x00\x00\x00\x00\x00\x00\x00\x00':
            print('No target1')
            target_1_status = False
        else:
            print('1_x:',target_1_x_distance/10,'CM')
            print('1_y:',target_1_y_distance/10,'CM')
            print('1_speed:',target_1_speed_distance/10,'CM/S')
            print('1_range:',target_1_Range_Resolution_num/10,'CM')
            target_1_status = True
        print('--------------------------------------')

        if target_2_data == b'\x00\x00\x00\x00\x00\x00\x00\x00':
            target_2_status = False
            print('No target2')
        else:
            print('2_x:',target_2_x_distance/10,'CM')
            print('2_y:',target_2_y_distance/10,'CM')
            print('2_speed:',target_2_speed_distance/10,'CM/S')
            print('2_range:',target_2_Range_Resolution_num/10,'CM')
            target_2_status = True
        print('----------------------------------------')

        if target_3_data == b'\x00\x00\x00\x00\x00\x00\x00\x00':
            target_3_status = False
            print('no target3')
        else:
            print('3_x:',target_3_x_distance/10,'CM')
            print('3_y:',target_3_y_distance/10,'CM')
            print('3_speed:',target_3_speed_distance/10,'CM/S')
            print('3_range:',target_3_Range_Resolution_num/10,'CM')
            target_3_status = True
        print('-----------------------------------------')
        if target_1_status != False:
            target_1_r = r(target_1_x_distance/10,target_1_y_distance/10)
        else:
            target_1_r = float('inf')
        if target_2_status != False:
            target_2_r = r(target_2_x_distance/10,target_2_y_distance/10)
        else:
            target_2_r = float('inf')
        if target_3_status != False:
            target_3_r = r(target_3_x_distance/10,target_3_y_distance/10)
        else:
            target_3_r = float('inf')

        current = min(target_1_r,target_2_r,target_3_r)
        print(current)
        if current <= 20:
            current = 100
        elif current > 20 and current <= 40:
            current = 80
        elif current > 40 and current <= 60:
            current = 60
        elif current > 60 and current <= 80:
            current = 40
        elif current > 80 and current < 100:
            current = 20
        elif current >= 100:
            current = 0
        led.duty_u16(int(current * 655.36))
        # if current >= led_duty :
            # while led_duty <= current-1:
            #     led_duty += 1
            #     led.duty_u16(int(led_duty * 655.36))
        # if current <= led_duty:
            # while led_duty >= current+1:
            #     led_duty -= 1
            #     led.duty_u16(int(led_duty * 655.36))

        time.sleep(0.1)