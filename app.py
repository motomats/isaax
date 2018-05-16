import time

while True:
    temp=float(open('/sys/class/thermal/thermal_zone0/temp').read().strip())/1000
    print("Temperature: %s C" % round(temp,2))
    time.sleep(60)
