import socket

HOST_server = ''
PORT_server = 2018

HOST_S ='192.168.240.225'
PORT_S =2017

socket_from_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_from_client.bind((HOST_server, PORT_server))
socket_from_client.listen(1)

socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while 1:
    print("Ready for a new connection!")
    conn, addr = socket_from_client.accept()
    print("Connected by", addr)
    socket_to_server.connect((HOST_S, PORT_S))

    while 1:
        data = conn.recv(10000)
        if not data:
            break
        datastringa = data.decode()
        print("Dati ricevuti: ", datastringa)
        socket_to_server.send(data)


        if datastringa == "ELENCO":
            print("Si trasferiscono i file presi nella directory del target")
            dati_ricevuti_server = socket_to_server.recv(4028)
            dati_ricevuti = dati_ricevuti_server.decode()
            print("Dati ricevuti dal server principale:", dati_ricevuti)
            conn.send(dati_ricevuti_server)

        if datastringa == "CIFRA SIMMETRICA":
            nomefile = conn.recv(1024)
            socket_to_server.send(nomefile)

            chiave = socket_to_server.recv(1024)
            conn.send(chiave)

            messaggio = socket_to_server.recv(1024)
            conn.send(messaggio)

        if datastringa == "CIFRA ASIMMETRICA":
            nomefile = conn.recv(1024)
            socket_to_server.send(nomefile)

            key = conn.recv(1024)
            socket_to_server.send(key)
            message = socket_to_server.recv(1024)
            conn.send(message)
            print("I dati sono stai inviati al Client")

    conn.close()