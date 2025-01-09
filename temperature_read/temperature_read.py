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

# Inicjalizacja czujników temperatury
sensor_1 = W1ThermSensor(sensor_id="0573b00a6461")
# Zakładając, że masz dwa czujniki i masz dostęp do ich unikalnych adresów
# Odczyt adresu drugiego czujnika, musisz znaleźć adres urządzenia.
# Możesz to zrobić za pomocą `sensor_1.get_available_sensors()` lub znać adresy z konfiguracji.

# Ustawienie czujnika 2
sensor_2 = W1ThermSensor(sensor_id="03977f1f64ff")  # Wstaw właściwy adres sensor_2

# Główna pętla
try:
    while True:
        # Odczyt temperatury z obu czujników
        temperature_1 = sensor_1.get_temperature()
        temperature_2 = sensor_2.get_temperature()

        # Wydruk temperatur
        print(f"Temperature 1: {temperature_1:.2f}°C")
        print(f"Temperature 2: {temperature_2:.2f}°C")

        # Jeśli temperatura przekroczy 25 stopni, zapal LED na GPIO17
        if temperature_1 > 25 or temperature_2 > 25:
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
