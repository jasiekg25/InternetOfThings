from VirtualCopernicus.VirtualCopernicusNG import TkCircuit
from VirtualCopernicus.Lab02 import config as config

CONFIGURATION = config.set_configuration("Lobby")

CIRCUIT = TkCircuit(CONFIGURATION)


@CIRCUIT.run
def main():
    from gpiozero import LED, Button
    from time import sleep

    SOCKET = config.set_socket()
    COMMAND = 'f1;*;lamp;*;off'

    def button2_pressed():
        SOCKET.sendto(COMMAND.encode(config.CODE), (config.MCAST_GRP, config.MCAST_PORT))
        led.off()

    led = LED(21)

    button1 = Button(11)
    button1.when_pressed = led.toggle

    button2 = Button(12)
    button2.when_pressed = button2_pressed

    while True:
        sleep(0.1)
