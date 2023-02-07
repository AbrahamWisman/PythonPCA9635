PCA9635 Driver

This is a python driver for the PCA9635 16-channel, 8-bit resolution LED driver.

Requirements
smbus
Usage
To use this driver, you must first create an instance of the PCA9635 class with the address of your device and the bus number that it is connected to.


`pca = PCA9635(0x60, bus=1)`
To check if your device is connected, you can use the is_connected() method.


`if pca.is_connected():
    print("Device is connected")
else:
    print("Device is not connected")`
You can set the mode of the device using the set_mode() method and read the current mode using the read_mode() method. The available modes are MODE1 and MODE2 and their values are defined as class variables.

`# Set the mode to MODE1
pca.set_mode(PCA9635.MODE1, PCA9635.ALLCALL)

# Read the current mode
mode = pca.read_mode(PCA9635.MODE1)`

You can set the driver mode of a specific channel using the set_driver_mode() method and read the current driver mode of a channel using the read_driver_mode() method. The available driver modes are OFF, ON, PWM, and GRPPWM and their values are defined as class variables.


`# Set the driver mode of channel 0 to PWM
pca.set_driver_mode(0, PCA9635.PWM)

# Read the current driver mode of channel 0
mode = pca.read_driver_mode(0)'
You can set the PWM value of a channel using the set_pwm() method. The channel must be between
0 and 15 and the value must be between 0 and 255.

