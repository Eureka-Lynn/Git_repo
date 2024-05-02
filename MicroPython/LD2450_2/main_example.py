import machine
import time

# 设置串口引脚（使用引脚0和1作为 tx 和 rx）
uart = machine.UART(0, baudrate=256000, tx=0, rx=1)

while True:
    data = uart.read()
    if data:
        hex = data[0:30]
        data_body = hex[5:29]
        target_x = data_body[0:8]
        target_y = data_body[8:16]
        target_z = data_body[16:24]
        
        target_x_xcoordinate = target_x[0:2]
        target_x_ycoordinate = target_x[2:4]
        target_x_speed = target_x[4:6]
        target_x_resolution = target_x[6:8]
        
        target_x_xcoordinate_mm = int.from_bytes(target_x_xcoordinate,'little')
        target_x_ycoordinate_mm = int.from_bytes(target_x_ycoordinate,'little')
        target_x_speed_cm = int.from_bytes(target_x_speed,'little')
        target_x_resolution_mm = int.from_bytes(target_x_resolution,'little')
        
        target_x_xcoordinate_bin = bin(target_x_xcoordinate_mm)
        target_x_ycoordinate_bin = bin(target_x_ycoordinate_mm)
        target_x_speed_bin = bin(target_x_speed_cm)
        target_x_resolution_bin = bin(target_x_resolution_mm)
        
        if target_x_xcoordinate_bin[2] == 1:
            if target_x_xcoordinate_mm > 32768:
                target_x_xcoordinate_mm = target_x_xcoordinate_mm - 32768
        elif target_x_xcoordinate_bin[2] == 0:
            if target_x_xcoordinate_mm > -32768:
                target_x_xcoordinate_mm = 0 - target_x_xcoordinate_mm + 32768
            else:
                target_x_xcoordinate_mm = 0 - target_x_xcoordinate_mm

        if target_x_ycoordinate_bin[2] == 1:
            if target_x_ycoordinate_mm > 32768:
                target_x_xcoordinate_mm = target_x_ycoordinate_mm - 32768
        elif target_x_ycoordinate_bin[2] == 0:
            if target_x_ycoordinate_mm > -32768:
                target_x_ycoordinate_mm = 0 - target_x_ycoordinate_mm + 32768
            else:
                target_x_ycoordinate_mm = 0 - target_x_ycoordinate_mm

        if target_x_speed_bin[2] == 0:
            target_x_speed_cm = -target_x_speed_cm
        
        print(target_x)
        print(target_x_xcoordinate)
        print(target_x_xcoordinate_bin)
        # 为什么我的数据如此抽象？
        # print('----------------------------------')
        # print('target_xcoordinate_cm',target_x_xcoordinate_mm/10,'cm')
        # print('target_ycoordinate_cm',target_x_ycoordinate_mm/10,'cm')
        # print('target_speed',target_x_speed_cm,'cm/s')
        # print('target_resolution',target_x_resolution_mm,'mm')
        print('---------------------------')
    time.sleep(1)