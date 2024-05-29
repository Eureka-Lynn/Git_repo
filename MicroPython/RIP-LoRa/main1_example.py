import time
import math
from machine import UART, Pin

# Initialize UART for LoRa communication
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Constants
MAX_DISTANCE = 100  # Maximum detection distance of the radar in centimeters
MAX_BRIGHTNESS = 100  # Maximum brightness of the lights

# Function to detect presence of a person using radar
def detect_person():
    # Simulate radar detection, replace with actual detection logic
    return True  # For demonstration purpose, always return True

# Function to get distance from radar
def get_distance():
    # Simulate distance measurement, replace with actual measurement logic
    if detect_person():
        return 50  # For demonstration purpose, return a fixed distance when person is detected
    else:
        return float('inf')  # For demonstration purpose, return infinity when no person is detected

# Function to generate a unique node_id based on time
def generate_node_id():
    return int(time.time() * 1000) % 10000

# Function to broadcast node_id and brightness
def broadcast_message(node_id, brightness):
    message = f'DISCOVERY:{node_id}:{brightness}'
    uart.write(message + '\n')

# Function to receive message from UART
def receive_message():
    if uart.any():
        message = uart.readline().decode('utf-8').strip()
        return message
    return None

# Function to adjust brightness based on distance
def adjust_brightness(distance):
    if math.isinf(distance):
        return MAX_BRIGHTNESS  # Set maximum brightness if no person is detected
    else:
        return min(MAX_BRIGHTNESS, MAX_BRIGHTNESS - distance)  # Adjust brightness based on distance

# Main function to discover neighbors and adjust brightness
def main():
    # Generate node ID
    node_id = generate_node_id()

    while True:
        # Get distance from radar
        distance = get_distance()

        # Broadcast node ID and brightness
        brightness = adjust_brightness(distance)
        broadcast_message(node_id, brightness)

        # Receive messages from other nodes
        while uart.any():
            message = receive_message()
            if message and message.startswith('DISCOVERY'):
                parts = message.split(':')
                neighbor_id = int(parts[1])
                neighbor_brightness = int(parts[2])
                # Calculate distance between nodes
                distance = abs(brightness - neighbor_brightness)
                # Adjust brightness based on distance
                adjusted_brightness = min(MAX_BRIGHTNESS, MAX_BRIGHTNESS - distance)
                print(f'Node {node_id} received brightness from Node {neighbor_id}: {neighbor_brightness}, adjusted brightness: {adjusted_brightness}')
        
        # Delay before next iteration
        time.sleep(1)

# Start the main function
main()
