import RPi.GPIO as GPIO
import time

# Set up the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin number for the light (GPIO17 in this example)
LIGHT_PIN = 17
GPIO.setup(LIGHT_PIN, GPIO.OUT)

# Toggle the light on and off every second
try:
    while True:
        GPIO.output(LIGHT_PIN, GPIO.HIGH)  # Turn the light on
        time.sleep(0.2)                      # Wait for 1 second
        GPIO.output(LIGHT_PIN, GPIO.LOW)   # Turn the light off
        time.sleep(0.2)                      # Wait for 1 second
except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    GPIO.cleanup()  # Clean up GPIO settings before exit
