# PCA9635 Driver

This is a python driver for the PCA9635 16-channel, 8-bit resolution LED driver.

## Note

Build according to this datasheet: 
https://www.nxp.com/docs/en/data-sheet/PCA9635.pdf


## Requirements

* smbus

## Usage

#### Initializing the Class

To initialize the PCA9635 class, you need to pass the address of the device on the I2C bus and the bus number that the device is connected to (default is bus 1).

    pca = PCA9635(0x60)

#### Checking Connection

Use the is_connected() method to check if the device is connected:

    pca.is_connected()

This method returns True if the device is connected, and False otherwise.

#### Reading Mode

Use the read_mode(mode) method to read the current value of the specified mode:

    pca.read_mode(PCA9635.MODE1)

The mode argument can be either PCA9635.MODE1 or PCA9635.MODE2.

#### Setting Mode

Use the set_mode(mode, config) method to set the specified mode:

    pca.set_mode(PCA9635.MODE1, PCA9635.SLEEP | PCA9635.SUB1 | PCA9635.SUB2 | PCA9635.SUB3 | PCA9635.ALLCALL)

The mode argument can be either PCA9635.MODE1 or PCA9635.MODE2. The config argument is a binary or operation of the available configurations.

##### Mode 1 configurations

Constant        | 0                   | 1
-------------   | -------------   | -------------
SLEEP           | Normal mode    | Low power mode. Oscillator off*
SUB1            | does not respond to I2C-bus subaddress 1 *   |  responds to I2C-bus subaddress 1
SUB2            | does not respond to I2C-bus subaddress 2 *   |  responds to I2C-bus subaddress 2
SUB3            | does not respond to I2C-bus subaddress 3 *   |  responds to I2C-bus subaddress 3
ALLCALL         | does not respond to LED All Call I2C-bus address.    | responds to LED All Call I2C-bus address*

*default

##### Mode 2 configurations

Constant        | 0                   | 1
-------------   | -------------   | -------------
BLINK           | group control = dimming.* | group control = blinking.
INVERT            | Output logic state not inverted. Value to use when no external driver used. Applicable when OE = 0. *|  Output logic state inverted. Value to use when external driver used. Applicable when OE = 0
STOP            | Outputs change on STOP command.*  |  Outputs change on ACK.
OUTPUT_DRV            | The 16 LED outputs are configured with an open-drain structure.    |  The 16 LED outputs are configured with a totem-pole structure.*

*default

Look in the datasheet on how to use OUTPUTNE10 and OUTPUTNE00.


#### Reading Driver Mode

Use the read_driver_mode(channel) method to read the driver mode of the specified channel:

    pca.read_driver_mode(0)
The channel argument must be a value between 0 and 15.

#### Setting Driver Mode

Use the set_driver_mode(channel, mode) method to set the driver mode of the specified channel:

    pca.set_driver_mode(0, PCA9635.PWM)
The channel must be a value between 0 and 15, and the mode argument must be either PCA9635.OFF, PCA9635.ON, PCA9635.PWM, or PCA9635.GRPPWM.

#### Setting PWM

Use the set_pwm(channel, pwm) method to set the PWM of the specified channel:

    pca.set_pwm(0, 128)

The channel argument must be a value between 0 and 15, and the pwm between 0 and 255.
