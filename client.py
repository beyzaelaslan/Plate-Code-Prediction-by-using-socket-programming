import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
guess = None

message = client_socket.recv(1024).decode('utf-8')
print(message)

while True:

    guess = input("Your guess:")
    client_socket.sendall(bytes(guess, 'utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    if guess == "END" or not response.startswith("You have entered"):
        client_socket.close()
        break

exit()
