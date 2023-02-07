import smbus


class PCA9635:
    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)

    def is_connected(self):
        try:
            bus = smbus.SMBus(1)
            bus.read_byte_data(self.address, 0x00)
            return True
        except:
            return False

    def read_mode(self, mode):
        if mode > 1 or mode < 0:
            raise ValueError("Invalid mode. Mode must be PCA9635.MODE1 or PCA9635.MODE2.")
        try:
            # Read the current value of the mode 1 register
            config = self._read_from_register(mode)
            return config
        except OSError as e:
            print("Error reading mode 1:", e)

    def set_mode(self, mode, config):
        if mode > 1 or mode < 0:
            raise ValueError("Invalid mode. Mode must be PCA9635.MODE1 or PCA9635.MODE2.")
        if config > 255 or config < 0:
            raise ValueError("Invalid config. Config must be between 0 and 255")
        try:
            self._write_to_register(mode, config)
        except OSError as e:
            print("Error setting mode 1:", e)

    def read_driver_mode(self, channel):
        if channel > 15 or channel < 0:
            raise ValueError("Invalid channel. Channels must be between 0 and 15.")
        try:
            # Read the current value of the LEDOUT0 or LEDOUT1 register
            ledout_reg = 0x14 + (channel // 4)
            ledout = self._read_from_register(ledout_reg)

            # Extract the driver mode bits of the specified LED
            mode = (ledout >> (2 * (channel % 4))) & 0x03

            return mode
        except OSError as e:
            print("Error reading driver mode:", e)

    def set_driver_mode(self, channel, mode):
        if channel > 15 or channel < 0:
            raise ValueError("Invalid channel. Channels must be between 0 and 15.")
        if mode > 3 or mode < 0:
            raise ValueError("Invalid mode. Mode must be between 0x00 and 0x03.")
        try:
            # Read the current value of the LEDOUT0 or LEDOUT1 register
            ledout_reg = 0x14 + (channel // 4)
            ledout = self._read_from_register(ledout_reg)

            # Calculate the bit mask for the driver mode bits of the specified LED
            mask = 0x03 << (2 * (channel % 4))

            # Update the value of the LEDOUT0 or LEDOUT1 register with the specified mode
            ledout &= ~mask
            ledout |= (mode << (2 * (channel % 4)))
            self._write_to_register(ledout_reg, ledout)
        except OSError as e:
            print("Error setting driver mode:", e)

    def set_pwm(self, channel, pwm):
        if channel > 15 or channel < 0:
            raise ValueError("Invalid channel. Channels must be between 0 and 15.")
        if pwm > 255 or pwm < 0:
            raise ValueError("Invalid value. Values must be between 0 and 255.")
        try:
            self._write_to_register(0x02 + channel, pwm)
        except OSError as e:
            print("Error setting channel pwm:", e)

    def _write_to_register(self, register_address, value):
        try:
            self.bus.write_byte_data(self.address, register_address, value)
        except IOError as e:
            raise IOError("Error writing to register: {}".format(e))

    def _read_from_register(self, register_address):
        try:
            return self.bus.read_byte_data(self.address, register_address)
        except IOError as e:
            raise IOError("Error reading from register: {}".format(e))

    # Modes
    MODE1 = 0x00
    MODE2 = 0x01

    # Mode 1 registers
    SLEEP = 0x10
    SUB1 = 0x08
    SUB2 = 0x04
    SUB3 = 0x02
    ALLCALL = 0x01

    # Mode 2 registers
    BLINK = 0x20
    INVERT = 0x10
    STOP = 0x08
    OUTPUT_DRV = 0x04
    OUTPUTNE10 = 0x02
    OUTPUTNE00 = 0x01

    # Channel Driver Modes
    OFF = 0x00  # default
    ON = 0x01
    PWM = 0x02
    GRPPWM = 0x03
