"""threading is a sequence of instruction within the program"""
import threading
import socket

host = '127.0.0.1'
port = 59000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []


def broadcast(message):
    for client in clients:
        client.send(message)

# Functions handle clients connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)  # 1024 maximum number of bites that the server can received form the client
            broadcast(message)
        except:
            index = client.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode())
            aliases.remove(alias)
            break

#Functions to receive the client connection
def receive():
    while True:
        print('Server is running and listening...')
        client, address = server.accept() #.accept() --> returns a new socket representing the connection and the add of the client
        print(f'Connections is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of the client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()