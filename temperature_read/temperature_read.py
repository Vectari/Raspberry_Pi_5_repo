import time
import sys
import RPi.GPIO as GPIO

# Dodajemy ścieżkę do w1thermsensor
sys.path.append('/home/vectari/Documents/GIT/Raspberry_Pi_5_repo/temperature_read/w1thermsensor/src')

from w1thermsensor import W1ThermSensor

# Ustawienie numeracji pinów GPIO
GPIO.setmode(GPIO.BCM)

# Ustawienie pinu GPIO17 jako wyjście
GPIO.setup(17, GPIO.OUT)

# Inicjalizacja czujnika temperatury
sensor = W1ThermSensor()

# Główna pętla
try:
    while True:
        # Odczyt temperatury w stopniach Celsjusza
        temperature = sensor.get_temperature()
        print(f"Temperature: {temperature:.2f}°C")

        # Jeśli temperatura przekroczy 25 stopni, zapal LED na GPIO17
        if temperature > 25:
            GPIO.output(17, GPIO.HIGH)  # Włączenie LED
        else:
            GPIO.output(17, GPIO.LOW)   # Wyłączenie LED

        # Czekaj 2 sekundy przed kolejnym odczytem
        time.sleep(2)

# Obsługa zakończenia programu
except KeyboardInterrupt:
    print("Program interrupted by user")

finally:
    # Zatrzymaj wszystkie piny GPIO przy wyjściu z programu
    GPIO.cleanup()
