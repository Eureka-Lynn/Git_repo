import machine
import time
uart = machine.UART(0, baudrate=256000, tx=machine.Pin(0), rx=machine.Pin(1))  # 根据实际情况修改引脚号

# 主循环
while True:
    # 接收雷达上报数据
    radar_data = uart.read()
    if radar_data:
        data = radar_data.hex()
        # target_data = radar_data[6:19]
        # target_status = target_data[2]
        target_distance = target_data[3:5]
        # target_energy = target_data[5:6]
        # static_target_distance = target_data[6:8]
        # static_target_energy = target_data[8:9]
        # detection_distancce = target_data[9:11]
        target_distance_cm = int.from_bytes(target_distance,'little')

        print(target_distance_cm)
        #f4f3f2f10d0002aa032f00641e006421005500f8f7f6f5
        data_length = data[8:12]
        data_in_frame = data[12:38]
        target_data = data_in_frame[4:22]
        target_state = target_data[0:2]
        target_distance = target_data[2:6]
        target_energy = target_data[6:8]
        static_target_distance = data[8:12]
        static_target_energy = data[12:14]
        detection_distance = data[14:18]
        dict = {'00':'no_target',
                '01':'moving_target',
                '02':'static_target',
                '03':'moving & static_target'}
        # 转换小端模式
        target_state = dict.get(target_state,'Unknow')
        target_distance_cm = int(target_distance[2:]+target_distance[:2],16)
        target_energy = int(target_energy,16)
        static_target_distance_cm = int(static_target_distance[2:]+static_target_distance[:2],16)
        static_target_energy = int(static_target_energy,16)
        detection_distance_cm = int(detection_distance[2:]+detection_distance[:2],16)
        target_distance_cm = int.from_bytes(target_distance[2:]+target_distance[:2],16)
        print('target_state',target_state)
        # print('target_distance',target_distance_cm,'cm')
        print('target_energy',target_energy)
        print('static_target_distance',static_target_distance_cm,'cm')
        print('static_target_energy',static_target_energy)
        print('detection_distance',detection_distance_cm,'cm')
        print('-----------------------------------')
    # 等待一段时间后再次接收数据
    time.sleep(0.1)
