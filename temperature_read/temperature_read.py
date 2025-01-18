import sys
import time


# Dodanie ścieżki do biblioteki (jeśli nie jest w standardowej lokalizacji)
sys.path.append('/home/vectari/Documents/GIT/Raspberry_Pi_5_repo/temperature_read/w1thermsensor/src')
from w1thermsensor import W1ThermSensor

# Inicjalizacja sensorów
sensors = W1ThermSensor.get_available_sensors()

# Sprawdzenie, czy wykryto jakiekolwiek czujniki
if not sensors:
    print("Nie znaleziono czujników temperatury.")
    sys.exit(1)

# Pętla odczytu
try:
    while True:
        for sensor in sensors:
            temperature = sensor.get_temperature()
            print(f"Czujnik {sensor.id}: {temperature:.2f}°C")
        time.sleep(1)  # Odczekanie 1 sekundy przed kolejnym odczytem
        print("-------")
except KeyboardInterrupt:
    print("\nZatrzymano odczyt temperatury.")




# Raspberry Pi GPIO4 (pin 7) ---> DQ (obie sondy) żółte
# Raspberry Pi 3.3V (pin 1) ----> VCC (obie sondy) czerwone
# Raspberry Pi GND (pin 6) -----> GND (obie sondy) czarne
# Rezystor 4.7kΩ pomiędzy VCC a DQ
