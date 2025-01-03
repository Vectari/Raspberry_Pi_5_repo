import os
import time

def get_cpu_temperature():
    # Read the CPU temperature from the system file
    temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    # Convert the temperature to Celsius
    return float(temp) / 1000

def main():
    try:
        while True:
            temp = get_cpu_temperature()
            print(f"CPU Temperature: {temp:.2f}°C")
            time.sleep(3)  # Wait for 1 second before updating
    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    main()
