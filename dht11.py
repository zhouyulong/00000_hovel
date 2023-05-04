import Adafruit_DHT as dht11
import time


def temper_humidity() -> None:
    sensor = dht11.DHT11

    gpio = 24

    humidity, temperature = dht11.read_retry(sensor, gpio)

    if humidity is not None and temperature is not None:
        print(f'humidity:    {humidity:.2f}%\t temperature:    {temperature:.2f}℃')
    else:
        print('Failed to get reading. Try again')

for i in range(10):
    time.sleep(5)
    temper_humidity()