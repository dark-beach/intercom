# run this on the computer that sends messages to server
import socket

SERVER_IP = "192.168.X.X"  # LLM's IP
PORT = 5000 # all port listen

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT)) # change to server's ip and port

command = "open_notepad"  # just a test command, has to match server main's command list
client_socket.send(command.encode("utf-8"))

response = client_socket.recv(1024).decode("utf-8")
print(f"Server response: {response}")

client_socket.close()