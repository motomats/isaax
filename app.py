import time
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)

while True:
    print("Hello IoT from Isaax")
    sense.show_message("Hello IoT from Isaax")
    time.sleep(60)
