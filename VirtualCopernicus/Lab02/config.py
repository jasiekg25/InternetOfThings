import socket
import struct

MCAST_GRP = '236.0.0.0'
MCAST_PORT = 3456
ANY = "*"
LAMP = "lamp"
ON = "on"
OFF = "off"
CHANGE = "change"
ONE = "1"
TWO = "2"
CODE = "utf-8"
SPLIT = ";"


def set_configuration(room_name):
    return {
        "name": room_name,
        "sheet": "sheet_smarthouse.png",
        "width": 332,
        "height": 300,
        "leds": [
            {"x": 112, "y": 70, "name": "LED 1", "pin": 21},
            {"x": 71, "y": 141, "name": "LED 2", "pin": 22}
        ],
        "buttons": [
            {"x": 242, "y": 146, "name": "Button 1", "pin": 11},
            {"x": 200, "y": 217, "name": "Button 2", "pin": 12},
        ],
        "buzzers": [
            {"x": 277, "y": 9, "name": "Buzzer", "pin": 16, "frequency": 440},
        ]
    }


def set_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    return sock
