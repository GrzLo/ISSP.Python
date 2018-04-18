import socket
import threading

# adres hosta (pusta nazwa = adresy lokalne), port, wielkosc bufora otrzymywanych danych
host = ''
port = 22221
bufferSize = 1024
# komunikat powitalny
welcomeMessage = "Welcome to Greg's server!\n" \
                 "Type any message to receive an echo response\n" \
                 "Type UPPER to convert any following message's characters to UPPERCASE\n" \
                 "Type LOWER to convert any following message's characters to lowercase\n" \
                 "To exit the UPPER or LOWER commands type a single dot in a new line and press ENTER\n" \
                 "To end the transmission type QUIT\n" \
                 "Have a pleasant stay!"


# funkcja obslugi klienta
def client_handling(cli, add):
    print("Connected established from:", add)
    cli.sendall(welcomeMessage.encode())
    # trzy typy pisania: 1 = standardowy = uzytkownik wpisuje jakis tekst a serwer wysyla odrazu echo
    #                    2,3 = lowercase, uppercase = uzytkownik wpisuje tekst do momentu wyjscie sekwencja end-of-data
    #                          w praktyce znaczy to tyle ze nalezy w nowej linijce wpisac kropke i wcisnac enter
    #                          nastepnie serwer wysyla echo z wszystkimi wielkimi badz malymi literami zaleznie od
    #                          wybranego trybu. Po wyjsciu tryb pisania przechodzi z powrotem w tryb standardowy
    typeMode = 1
    while True:
        try:
            # sprawdzenie czy klient jest nadal polaczony z serwerem
            dataReceived = cli.recv(bufferSize)
            if not dataReceived:
                print("Client", add, "disconnected")
                cli.close()
                break
            else:
                # analiza otrzymanych danych od klienta i przejscie do wlasciwego trybu badz zakonczenie polaczenia
                dataReceivedDecoded = dataReceived.decode()
                if dataReceivedDecoded == "QUIT":
                    print("Client", add, "disconnected")
                    cli.sendall("Hope to see you soon! Bye!".encode())
                    cli.close()
                    break
                elif dataReceivedDecoded == "LOWER":
                    typeMode = 2
                    cli.sendall("Type mode was set to lowercase.\nPlease type your message.\n"
                                "To finish, type a single dot in a new line and press ENTER".encode())
                elif dataReceivedDecoded == "UPPER":
                    typeMode = 3
                    cli.sendall("Type mode was set to UPPERCASE.\nPlease type your message.\n"
                                "To finish, type a single dot in a new line and press ENTER".encode())
                else:
                    # echo serwera w zaleznosci od wybranego trybu
                    print("Received message from", add, ":", dataReceivedDecoded)
                    if typeMode == 1:
                        cli.sendall(("Server's echo response: {}".format(dataReceivedDecoded)).encode())
                    elif typeMode == 2:
                        cli.sendall(("Server's echo response: {}".format(dataReceivedDecoded.lower())).encode())
                        typeMode = 1
                        cli.sendall("\nType mode was set to default".encode())
                    elif typeMode == 3:
                        cli.sendall(("Server's echo response: {}".format(dataReceivedDecoded.upper())).encode())
                        typeMode = 1
                        cli.sendall("\nType mode was set to default".encode())

        except socket.error:
            cli.close()
            return False


# upewnienie się (i wymuszenie) ze port miesci sie w uprawnionym zakresie
while not 1024 <= port <= 65535:
    try:
        port = int(input("Wrong port number! Please enter a port number in the range of 1024-65535\n"))
    except ValueError:
        pass

# stworzenie socketu, AF_INET = protokol IPv4, SOCK_STREAM = socket typu TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketInstance:
    # zbindowanie socketu do adresu
    try:
        socketInstance.bind((host, port))
    # w razie niepoprawnego hosta zwraca komunikat o bledzie
    except (OSError, socket.gaierror) as e:
        if e.errno in (-2, 99):
            print("Wrong host address")

    # nasluchiwanie nadchodzacych polaczen
    socketInstance.listen(5)
    # glowna petla programu, laczenie sie z klientami, mozliwosc kilku niezaleznych polaczen naraz
    while True:
        client, address = socketInstance.accept()
        # client.settimeout(120) // mozna opcjonalnie wlaczyc
        threading.Thread(target=client_handling, args=(client, address)).start()
