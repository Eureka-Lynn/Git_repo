from machine import UART,Pin,PWM
import time
uart = UART(0, baudrate=256000, tx=Pin(0), rx=Pin(1))
led = PWM(Pin(6,Pin.OUT))
led.freq(1000)
led_duty = 0

while True:
    data = uart.read()
    if data:
        target_data = data[4:19]
        target_data_length = target_data[0:2]
        target_data_in_frame = target_data[2:]
        target_data_data = target_data_in_frame[2:11].hex()
        dict = {'00':'no_target',
                '01':'moving_target',
                '02':'static_target',
                '03':'moving & static_target'}
        target_state = target_data_data[0:2]
        moving_target_distance = target_data_data[2:6]
        moving_target_energy = target_data_data[7]
        static_target_distance = target_data_data[8:12]
        static_target_energy = target_data_data[13]
        detection_distance = target_data_data[14:18]

        target_state = dict.get(target_state,'unknow')
        moving_target_distance_cm = int(moving_target_distance[2:]+moving_target_distance[:2],16)
        moving_target_energy = int(moving_target_energy,16)
        static_target_distance_cm = int(static_target_distance[2:]+static_target_distance[:2],16)
        static_target_energy = int(static_target_energy,16)
        detection_distance_cm = int(detection_distance[2:]+detection_distance[:2],16)
        print('Target_state',target_state)
        print('Moving_target_distance',moving_target_distance_cm)
        print('Moving_target_energy',moving_target_energy)
        print('Static_target_distance',static_target_distance_cm)
        print('Static_target_energy',static_target_energy)
        print('Detection_distance',detection_distance_cm)
        time.sleep(0.1)
        current = 120 - detection_distance_cm
        if current < 0:
            current = 0
        if current >= led_duty :
            while led_duty <= current-1:
                led_duty += 1
                led.duty_u16(int(led_duty * 655.36))
        if current <= led_duty:
            while led_duty >= current+1:
                led_duty -= 1
                led.duty_u16(int(led_duty * 655.36))
        print('LED_DUTY',led_duty)
        time.sleep(0.1)