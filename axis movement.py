import pygame
import serial
import time

# Initialize Pygame
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick detected. Connect your PS3 controller.")
    pygame.quit()
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Connected Joystick: {joystick.get_name()}")

# Set up Serial connection with Arduino
arduino = serial.Serial('COM6', 9600)  # Change 'COM6' to match your Arduino port
time.sleep(2)  # Allow time for connection

prev_command_x = 'S'
prev_command_y = 'S'

try:
    while True:
        pygame.event.pump()  # Process events

        # Read joystick values (-1 to 1)
        left_x = joystick.get_axis(0)   # Left joystick (X-axis control)
        right_y = joystick.get_axis(3)  # Right joystick (Y-axis control)

        # Threshold to avoid small unwanted movements
        threshold = 0.2

        # Determine X-axis movement (Stepper X)
        if left_x > threshold:
            command_x = 'X'  # Move X forward
        elif left_x < -threshold:
            command_x = 'x'  # Move X backward
        else:
            command_x = 'S'  # Stop X motor

        # Determine Y-axis movement (Stepper Y)
        if right_y > threshold:
            command_y = 'Y'  # Move Y forward
        elif right_y < -threshold:
            command_y = 'y'  # Move Y backward
        else:
            command_y = 'S'  # Stop Y motor

        # Send commands only if they changed
        if command_x != prev_command_x:
            arduino.write(command_x.encode())
            print(f"Sent X Command: {command_x}")
            prev_command_x = command_x

        if command_y != prev_command_y:
            arduino.write(command_y.encode())
            print(f"Sent Y Command: {command_y}")
            prev_command_y = command_y

        pygame.time.delay(50)  # Prevent excessive CPU usage

except KeyboardInterrupt:
    print("Exiting...")
finally:
    arduino.close()
    pygame.quit()
