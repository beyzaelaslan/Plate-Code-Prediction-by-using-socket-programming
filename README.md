# Plate-Code-Prediction-by-using-socket-programming


In This Project, I developed an application using TCP socket programming.

Client Side:

Reads an Excel file containing license plates via the server.
Establishes a connection to the server.
Prompts the user to guess the license plate code of a city randomly selected by the server.
If the guess is correct or incorrect, the client socket to the server closes and the program terminates.
If the user enters "END," both the client-side and server-side processes terminate.
Server Side:

Waits for the client's connection and takes action when a client connects.
Selects a city randomly and asks the client for its license plate code.
If the guess is the license plate code of another city, responds with the name of the incorrectly guessed city.
If the guess is less than 1, greater than 81, or does not contain numeric data, sends an error message and closes the connection.
Waits for another client after handling each guess.
If the guess is correct, sends a success message and closes the connection.
If the user responds with "END," the server terminates the process.
This project demonstrates basic TCP socket communication, user interaction, and error handling in a client-server application.
