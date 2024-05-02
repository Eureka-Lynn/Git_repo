import machine
import time

uart = machine.UART(0, baudrate=256000, tx=0, rx=1)

while True:
    data = uart.read()
    if data:
        data = data[0:30]
        data_in_frame = data[4:28]
        target_1_data = data_in_frame[0:8]
        target_2_data = data_in_frame[8:16]
        target_3_data = data_in_frame[16:24]

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

        target_1_x_bin = bin(target_1_x_num)
        target_1_y_bin = bin(target_1_y_num)
        target_1_speed_bin = bin(target_1_speed_num)

        target_1_y_distance = '0'
        target_2_y_distance = '0'
        target_3_y_distance = '0'
        if target_1_x_bin[2] == '1':
            if target_1_x_num > 32768:
                target_1_x_distance = target_1_x_num - 32768
            else:
                target_1_x_distance = target_1_x_num
        else:
            target_1_x_distance = 0 - target_1_x_num

        if target_1_y_bin[2] == '1':
            if target_1_y_num > 32768:
                target_1_y_distance = target_1_y_num - 32768
            else:
                target_1_y_distance = target_1_y_num
        else:
            target_1_x_distance = 0 - target_1_x_num

        if target_1_speed_bin[2] == '1':
            if target_1_speed_num > 32768:
                target_1_speed_distance = target_1_speed_num - 32768
            else:
                target_1_speed_distance = target_1_speed_num
        else:
            target_1_speed_distance = 0 - target_1_speed_num

        target_2_x_bin = bin(target_2_x_num)
        target_2_y_bin = bin(target_2_y_num)
        target_2_speed_bin = bin(target_2_speed_num)

        if target_2_x_bin[2] == '1':
            if target_2_x_num > 32768:
                target_2_x_distance = target_2_x_num - 32768
            else:
                target_2_x_distance = target_2_x_num
        else:
            target_2_x_distance = 0 - target_2_x_num

        if target_2_y_bin[2] == '1':
            if target_2_y_num > 32768:
                target_2_y_distance = target_2_y_num - 32768
            else:
                target_2_y_distance = target_2_y_num
        else:
            target_2_x_distance = 0 - target_2_x_num

        if target_2_speed_bin[2] == '1':
            if target_2_speed_num > 32768:
                target_2_speed_distance = target_2_speed_num - 32768
            else:
                target_2_speed_distance = target_2_speed_num
        else:
            target_2_speed_distance = 0 - target_2_speed_num

        target_3_x_bin = bin(target_3_x_num)
        target_3_y_bin = bin(target_3_y_num)
        target_3_speed_bin = bin(target_3_speed_num)

        if target_3_x_bin[2] == '1':
            if target_3_x_num > 32768:
                target_3_x_distance = target_3_x_num - 32768
            else:
                target_3_x_distance = target_3_x_num
        else:
            target_3_x_distance = 0 - target_3_x_num

        if target_3_y_bin[2] == '1':
            if target_3_y_num > 32768:
                target_3_y_distance = target_3_y_num - 32768
            else:
                target_3_y_distance = target_3_y_num
        else:
            target_3_x_distance = 0 - target_3_x_num

        if target_3_speed_bin[2] == '1':
            if target_3_speed_num > 32768:
                target_3_speed_distance = target_3_speed_num - 32768
            else:
                target_3_speed_distance = target_3_speed_num
        else:
            target_3_speed_distance = 0 - target_3_speed_num

        if target_1_data == b'\x00\x00\x00\x00\x00\x00\x00\x00':
            print('No target1')
        else:
            print('1_x',target_1_x_distance/10,'CM')
            print('1_y',target_1_y_distance/10,'CM')
            print('1_speed',target_1_speed_distance/10,'CM')
            print('1_range',target_1_Range_Resolution_num/10,'CM')
        print('--------------------------------------')

        if target_2_data == b'\x00\x00\x00\x00\x00\x00\x00\x00':
            print('No target2')
        else:
            print('2_x',target_2_x_distance/10,'CM')
            print('2_y',target_2_y_distance/10,'CM')
            print('2_speed',target_2_speed_distance/10,'CM')
            print('2_range',target_2_Range_Resolution_num/10,'CM')
        print('----------------------------------------')

        if target_3_data == b'\x00\x00\x00\x00\x00\x00\x00\x00':
            print('no target3')
        else:
            print('3_x',target_3_x_distance/10,'CM')
            print('3_y',target_3_y_distance/10,'CM')
            print('3_speed',target_3_speed_distance/10,'CM')
            print('3_range',target_3_Range_Resolution_num/10,'CM')
        print('-----------------------------------------')
        
        time.sleep(0.1)