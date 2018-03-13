import time
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)

while True:
    print("Hello IoT from Isaax")
    sense.show_message("Hello IoT from Isaax")
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
    time.sleep(60)
