import time
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)

while True:
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
    sense.show_message("Temp: %s C" % temp)
    time.sleep(60)
