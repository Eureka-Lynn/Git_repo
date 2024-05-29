import time
from machine import UART, Pin

# Initialize UART for LoRa communication
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Generate a unique node_id based on time
def generate_node_id():
    return int(time.time() * 1000) % 10000

def broadcast_message(node_id, brightness):
    message = f'DISCOVERY:{node_id}:{brightness}'
    uart.write(message + '\n')

def receive_message():
    if uart.any():
        message = uart.readline().decode('utf-8').strip()
        return message
    return None

def discover_neighbors(node_id, brightness):
    broadcast_message(node_id, brightness)
    discovery_start_time = time.time()
    discovery_period = 0.2  # seconds
    while time.time() - discovery_start_time < discovery_period:
        received_data = receive_message()
        if received_data and received_data.startswith('DISCOVERY'):
            parts = received_data.split(':')
            neighbor_id = int(parts[1])
            neighbor_brightness = int(parts[2])
            distance = abs(brightness - neighbor_brightness)  # Example distance calculation
            # Adjust brightness based on distance (example logic)
            adjusted_brightness = 100 - distance * 10  # Example adjustment
            print(f'Node {node_id} received brightness from Node {neighbor_id}: {neighbor_brightness}, distance: {distance}, adjusted brightness: {adjusted_brightness}')
        time.sleep(1)

# Discover neighbors at startup
node_id = generate_node_id()  # Generate node ID based on time
brightness = 80  # Initial brightness
discover_neighbors(node_id, brightness)
