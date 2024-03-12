import time
import board

# pylint:disable=no-member
from adafruit_lsm6ds import Rate, AccelRange, GyroRange
from adafruit_register.i2c_bits import RWBits
from adafruit_register.i2c_bit import RWBit, ROBit
from micropython import const
from adafruit_bus_device import i2c_device
import busio # type: ignore


from adafruit_lsm6ds.lsm6dsox import LSM6DSOX 


sda_pin = board.GP16
scl_pin = board.GP17



i2c = busio.I2C(scl=scl_pin,sda=sda_pin)

sensor = LSM6DSOX(i2c)

sensor.low_pass_filter = 1

print("done")

class I2CWrapper:
    i2c_device = i2c_device.I2CDevice(i2c, 0x6A)
    control_register = RWBits(3, _LSM6DS_CTRL8_XL, 0)
    
print(I2CWrapper.control_register.__get__(I2CWrapper))