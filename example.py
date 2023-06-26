from PCA9635 import PCA9635

# Initialize the PCA9635 instance with the desired address and bus number
pca = PCA9635(address=0x40, bus=1)

# Check if the PCA9635 is connected
if pca.is_connected():
    print("PCA9635 device is connected.")
else:
    print("PCA9635 device is not connected.")

pca.set_mode(PCA9635.MODE1, 0b00000000)
print("New mode 1 configuration set.")

# Read the mode 1 configuration
mode1_config = pca.read_mode(PCA9635.MODE1)
print("Mode 1 configuration:", mode1_config)

pca.set_mode(PCA9635.MODE2, 0b00010100)
print("New mode 2 configuration set.")

# Read the mode 1 configuration
mode2_config = pca.read_mode(PCA9635.MODE2)
print("Mode 2 configuration:", mode2_config)


# Set a new driver mode for channels
for i in range(16):
    pca.set_driver_mode(i, PCA9635.PWM)
    driver_mode = pca.read_driver_mode(i)
    print(f"Driver mode for channel {i}: {driver_mode}")


def set_all(value):
    for i in range(16):
        pca.set_pwm(i, value)


set_all(0)
pca.set_pwm(15, 255)
