from VirtualCopernicus.VirtualCopernicusNG import TkCircuit
from VirtualCopernicus.Lab02 import config as config


CONFIGURATION = config.set_configuration("Living room")

CIRCUIT = TkCircuit(CONFIGURATION)


@CIRCUIT.run
def main():
    from gpiozero import LED, Button

    SOCKET = config.set_socket()
    FLOOR = 'f1'
    ROOM = 'living_room'
    COMMAND = 'f1;kitchen;lamp;1;change'

    def button2_pressed():
        SOCKET.sendto(COMMAND.encode(config.CODE), (config.MCAST_GRP, config.MCAST_PORT))

    led = LED(21)

    button1 = Button(11)
    button1.when_pressed = led.toggle

    button2 = Button(12)
    button2.when_pressed = button2_pressed

    while True:
        command = SOCKET.recv(10240).decode(config.CODE).split(config.SPLIT)
        print(command)
        if command[0] == FLOOR or command[0] == config.ANY:
            if command[1] == ROOM or command[1] == config.ANY:
                if command[2] == config.LAMP or command[2] == config.ANY:
                    if command[3] == config.ONE or command[3] == config.ANY:
                        if command[4] == config.ON:
                            led.on()
                        elif command[4] == config.ON:
                            led.off()
                        elif command[4] == config.CHANGE:
                            led.toggle()