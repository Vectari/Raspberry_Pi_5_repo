import time
import sys
import RPi.GPIO as GPIO
from flask import Flask, render_template

sys.path.append('/home/vectari/Documents/GIT/Raspberry_Pi_5_repo/temp_web/w1thermsensor/src')

from w1thermsensor import W1ThermSensor

# Ustawienie numeracji pinów GPIO
GPIO.setmode(GPIO.BCM)

# Ustawienie pinu GPIO17 jako wyjście
GPIO.setup(17, GPIO.OUT)

# Inicjalizacja czujników temperatury
sensor_1 = W1ThermSensor(sensor_id="0573b00a6461")
sensor_2 = W1ThermSensor(sensor_id="03977f1f64ff")  # Ustaw właściwy adres czujnika

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

@app.route('/')
def index():
    # Odczyt temperatur z czujników
    temperature_1 = sensor_1.get_temperature()
    temperature_2 = sensor_2.get_temperature()

    # Wydruk temperatur (opcjonalnie do konsoli)
    print(f"Temperature 1: {temperature_1:.2f}°C")
    print(f"Temperature 2: {temperature_2:.2f}°C")

    # Wysyłanie temperatur do strony
    return render_template('index.html', temp1=temperature_1, temp2=temperature_2)

@app.route('/check_led')
def check_led():
    # Odczyt temperatur z czujników
    temperature_1 = sensor_1.get_temperature()
    temperature_2 = sensor_2.get_temperature()

    # Zapalanie LED, jeśli którakolwiek z temperatur przekroczy 25°C
    if temperature_1 > 25 or temperature_2 > 25:
        GPIO.output(17, GPIO.HIGH)  # Włączenie LED
    else:
        GPIO.output(17, GPIO.LOW)   # Wyłączenie LED

    return 'LED state updated'

if __name__ == '__main__':
    try:
        # Uruchomienie serwera Flask na porcie 5000
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("Program interrupted by user")
    finally:
        # Zatrzymaj wszystkie piny GPIO przy wyjściu z programu
        GPIO.cleanup()
