import socket
import errno

# adres hosta (pusta nazwa = adresy lokalne), port, wielkosc bufora otrzymywanych danych
host = ''
# port musi byc identyczny jak port serwera
port = 22221
bufferSize = 1024
successfullyBinded = 0

# upewnienie się (i wymuszenie) ze port miesci sie w uprawnionym zakresie
while not 1024 <= port <= 65535:
    try:
        port = int(input("Wrong port number! Please enter a port number in the range of 1024-65535\n"))
    except ValueError:
        pass

# stworzenie socketu, AF_INET = protokol IPv4, SOCK_STREAM = socket typu TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketInstance:
    # proba polaczenia z serwerem
    try:
        socketInstance.connect((host, port))
    # komunikat o bledzie gdy klient nie moze sie polaczyc z serwerem
    except OSError as e:
        if e.errno == errno.ENOTCONN:
            print("Couldn't establish a connection to the server")
    while True:
        # odbior wiadomosci od serwera, oraz pobranie danych od uzytkownika
        try:
            dataReceived = socketInstance.recv(bufferSize)
            print(dataReceived.decode())
            dataSent = input()

            # odbior wiadomosci pozegnalnej od serwera oraz zamkniecie skryptu(nie jest to oczywiscie konieczne)
            if dataSent == "QUIT":
                socketInstance.sendall(dataSent.encode())
                dataReceived = socketInstance.recv(bufferSize)
                print(dataReceived.decode())
                break
            # wpisanie UPPER, LOWER powoduje pobieranie od uzytkownika danych az do wyslania w osobnej linijce kropki
            elif dataSent in ("UPPER", "LOWER"):
                socketInstance.sendall(dataSent.encode())
                dataReceived = socketInstance.recv(bufferSize)
                print(dataReceived.decode())
                dataSent = " "
                newline = input()
                while newline != ".":
                    dataSent += "\n" + newline
                    newline = input()
                socketInstance.sendall(dataSent.encode())
            else:
                socketInstance.sendall(dataSent.encode())

        except OSError as e:
            if e.errno == errno.ENOTCONN:
                print("Couldn't establish a connection to the server")
                break
