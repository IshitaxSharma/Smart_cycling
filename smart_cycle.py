import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

# Set up GPIO pins for ultrasonic sensor
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Initialize variables
distances = []
cycle_count = 0
min_distance = float('inf')  # Set initial minimum distance to infinity

# Define a function to calculate distance from the ultrasonic sensor
def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

# Infinite loop to continuously measure distances and update the graph
while True:
    distance = get_distance()
    distances.append(distance)
    if distance < min_distance:
        min_distance = distance
        cycle_count += 1
    plt.plot(distances)
    plt.xlabel('Time (s)')
    plt.ylabel('Distance (cm)')
    plt.title('Ultrasonic Sensor Readings')
    plt.draw()
    plt.pause(0.001)
    plt.clf()  # Clear the graph to avoid overplotting
    print("Cycle count: ", cycle_count)