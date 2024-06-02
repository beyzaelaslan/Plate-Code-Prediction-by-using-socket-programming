import socket
import random
import pandas as pd


def read_plate_codes(filename):
    df = pd.read_excel(filename)
    return dict(zip(df['CityName'], df['PlateNumber']))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
plate_codes = read_plate_codes('plate_list.xlsx')
client_counter = 1
cities = list(plate_codes.keys())

while True:

    print(f"Waiting for {client_counter}th client connection.")
    print("Server is waiting for connection...")

    client_socket, addr = server_socket.accept()
    print("Client connected from: ", addr)
    client_counter += 1

    chosen_city = random.choice(cities)
    client_socket.sendall(bytes("What is the plate code of {}".format(chosen_city), 'utf-8'))

    while True:

        guess = client_socket.recv(1024).decode('utf-8')
        print("Received from client: ", guess)

        if guess == "END":
            client_socket.close()
            server_socket.close()
            exit()

        elif not guess.isdigit():
            client_socket.sendall(bytes("You entered a non-numeric value. Game Over.", 'utf-8'))
            break

        elif int(guess) < 1 or int(guess) > 81:
            client_socket.sendall(bytes("Number exceeds the range. Game Over.", 'utf-8'))
            break

        elif int(guess) == plate_codes[chosen_city]:
            client_socket.sendall(bytes("Correct!", 'utf-8'))
            break

        else:
            if int(guess) in plate_codes.values():
                city = [key for key, value in plate_codes.items() if value == int(guess)][0]
                client_socket.sendall(bytes("You have entered the plate code of {}.".format(city), 'utf-8'))

    client_socket.close()
