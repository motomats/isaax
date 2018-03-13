import time
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)

while True:
    temp = sense.get_temperature()
    print("Temperature: %s C" % round(temp,2))
    sense.show_message("Temp: %s C" % round(temp,2))
    time.sleep(60)
