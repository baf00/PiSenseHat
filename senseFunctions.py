from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.set_imu_config(True,True,True)  # all functions on

orientation_rad = sense.get_orientation_radians()


direction = sense.orientation_radians
print("Direction: %s radians" % direction)


sense.show_message("Direction: %s radians" % direction, scroll_speed=.05)

temp = sense.get_temperature()
print("Temperature: %s C" % temp)
tempf = (9.0/5.0 * temp) + 32
print("Temperature: %s F" % tempf)

humidity = sense.get_humidity()



print("Humidity: %s %%rH" % humidity)

sense.show_message("Temperature: %s C" % temp)
