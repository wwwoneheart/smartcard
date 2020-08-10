from websocket_server import WebsocketServer
from smartcard.System import readers


# Called when a client sends a message
def message_received(client, server, message):
    if message == "GetInfo":
        try:
            Select = [0xFF, 0xA4, 0x00, 0x00, 0x01, 0x06]
            ReadName = [0xFF, 0xB0, 0x00, 0x20, 0x09]
            ReadBirthday = [0xFF, 0xB0, 0x00, 0x30, 0x08]
            ReadID = [0xFF, 0xB0, 0x00, 0x40, 0x0A]

            r = readers()
            reader = r[0]

            connection = reader.createConnection()
            connection.connect()

            connection.transmit(Select)

            send_data = ''
            data, sw1, sw2 = connection.transmit(ReadName)
            send_data += bytes(data).decode('utf8') + ","
            data, sw1, sw2 = connection.transmit(ReadBirthday)
            send_data += ''.join(chr(i) for i in data) + ","
            data, sw1, sw2 = connection.transmit(ReadID)
            send_data += ''.join(chr(i) for i in data) + "\n"

            server.send_message_to_all(send_data)
        except:
            server.send_message_to_all('error')


PORT = 9981
server = WebsocketServer(PORT)
server.set_fn_message_received(message_received)
server.run_forever()