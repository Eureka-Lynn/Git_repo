import time
from machine import UART, Pin, PWM

# Initialize UART for LoRa communication
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

node_id = None  # Unique node ID, will be assigned dynamically
neighbors = {}  # Dictionary to store neighbors' information

# Initialize PWM for LED control
led = PWM(Pin(15))
led.freq(1000)

def set_led_brightness(brightness):
    duty_cycle = int(brightness * 1023 / 100)
    led.duty(duty_cycle)

def broadcast_message(message):
    uart.write(message + '\n')

def receive_message():
    if uart.any():
        message = uart.readline().decode('utf-8').strip()
        return message
    return None

def assign_node_id():
    global node_id
    node_id = int(time.time() * 1000) % 10000  # Simple unique ID based on timestamp

def update_neighbors():
    current_time = time.time()
    for neighbor_id in list(neighbors.keys()):
        if current_time - neighbors[neighbor_id]['timestamp'] > 10:  # 10 seconds timeout
            del neighbors[neighbor_id]

def send_updates():
    neighbor_ids = ','.join(map(str, neighbors.keys()))
    broadcast_message(f'UPDATE:{node_id}:{neighbor_ids}')

def process_updates():
    received_data = receive_message()
    if received_data and received_data.startswith('UPDATE'):
        parts = received_data.split(':')
        neighbor_id = int(parts[1])
        received_neighbors = parts[2].split(',')
        neighbors[neighbor_id] = {'timestamp': time.time(), 'neighbors': received_neighbors}

def calculate_brightness():
    brightness = 80  # Base brightness
    for neighbor_id, info in neighbors.items():
        distance = abs(node_id - neighbor_id) * 10  # Example distance calculation
        if distance < 50:
            brightness = max(brightness, 100)
        elif distance < 100:
            brightness = max(brightness, 80)
    set_led_brightness(brightness)

assign_node_id()

while True:
    update_neighbors()
    send_updates()
    process_updates()
    calculate_brightness()
    time.sleep(1)
