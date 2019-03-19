from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import json
import settings
import models as mo


HOST = settings.TCP_HOST
PORT = settings.TCP_PORT
BUFFER_SIZE = settings.TCP_BUFFER_SIZE
BYTE_ORDER = settings.TCP_BYTE_ORDER

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen()
    print("Server listening at {}:{}".format(HOST, PORT))
    while True:
        (conn, addr) = sock.accept()
        print("Connection received from {}:{}".format(*addr))
        msg_lenght = conn.recv(BUFFER_SIZE)
        lenght_bytes = int.from_bytes(msg_lenght, byteorder=BYTE_ORDER)
        msg = json.loads(conn.recv(lenght_bytes))

        msg_type = msg.get("Msg type", None)

        reponse = {}

        if msg_type == "STATS":

            reponse = {"Msg type": "ACK", "Msg ID": msg["Msg ID"]}

        if msg_type == "CONFIG":

            recup_config_server = mo.GameServer.get(mo.GameServer.nom_serveur == msg["Machine name"])
            reponse_config = recup_config_server.get_config(msg["Msg ID"])

        reponse_config = json.dumps(reponse)
        msg_encode_config = bytes(reponse_config.encode("utf-8"))
        first_bytes = len(msg_encode_config).to_bytes(BUFFER_SIZE, byteorder=BYTE_ORDER)
        full_message = first_bytes + msg_encode_config
        conn.send(full_message)

        conn.close()
