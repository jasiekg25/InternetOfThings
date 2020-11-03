from VirtualCopernicus.VirtualCopernicusNG import TkCircuit
from VirtualCopernicus.Lab02 import config as config

CONFIGURATION = config.set_configuration("Bedroom")

CIRCUIT = TkCircuit(CONFIGURATION)


@CIRCUIT.run
def main():
    from gpiozero import LED, Button

    SOCKET = config.set_socket()
    FLOOR = 'f1'
    ROOM = 'bedroom'

    led1 = LED(21)
    led2 = LED(22)

    button1 = Button(11)
    button1.when_pressed = led1.toggle
    button2 = Button(12)
    button2.when_pressed = led2.toggle

    while True:
        command = SOCKET.recv(10240).decode(config.CODE).split(config.SPLIT)
        print(command)
        if command[0] == FLOOR or command[0] == config.ANY:
            if command[1] == ROOM or command[1] == config.ANY:
                if command[2] == config.LAMP or command[2] == config.ANY:
                    if command[3] == config.ONE or command[3] == config.ANY:
                        if command[4] == config.ON:
                            led1.on()
                        elif command[4] == config.OFF:
                            led1.off()
                        elif command[4] == config.CHANGE:
                            led1.toggle()
                    if command[3] == config.TWO or command[3] == config.ANY:
                        if command[4] == config.ON:
                            led2.on()
                        elif command[4] == config.OFF:
                            led2.off()
                        elif command[4] == config.CHANGE:
                            led2.toggle()
