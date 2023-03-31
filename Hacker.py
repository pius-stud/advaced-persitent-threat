import socket
from cryptography.fernet import Fernet
import rsa

HOST = '192.168.240.225'
PORT = 2018
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("La lista di comandi da poter eseguire sono: STOP, ELENCO, CIFRA SIMMETRICA e CIFRA ASIMMETRICA")

while 1:
    messaggio = input("Inserisci messaggio:")
    s.send(messaggio.encode())

    if (messaggio=="STOP"):
        break

# Il comando ELENCO restituisce i file presenti all'interno della directory corrente del target
    if (messaggio=="ELENCO"):
        messaggioRicevuto = s.recv(2048)
        files = eval(messaggioRicevuto)
        print("File presenti:")
        for i in files:
            print(i)

    if (messaggio == "CIFRA SIMMETRICA"):
        nomefile = input('Inserire nome file:')
        s.send(nomefile.encode())
        key = s.recv(1024)
        encMsg = s.recv(1024)
        message = encMsg.decode()
        print("File cifrato: " + message)

        fernet = Fernet(key)

        decMsg = fernet.decrypt(encMsg)
        print("File decifrato: ", decMsg.decode())

    if (messaggio == "CIFRA ASIMMETRICA"):
        nomefile = input('Inserire nome file:')
        s.send(nomefile.encode())

        publicKey, privateKey = rsa.newkeys(512)
        s.send(publicKey.save_pkcs1())

        message = s.recv(1024)
        print("Il messaggio cifrato è:", message)
        decr_message = rsa.decrypt(message, privateKey).decode()
        print("Il messaggio decifrato è:", decr_message)

s.close()
