# run this on server
# listens to incoming messages and executes accordingly
import socket

HOST = "0.0.0.0"  # listen to all net interfaces
PORT = 5000  # any free port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

# just confirmation listening succeeded
print(f"Listening on {HOST}:{PORT}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    data = client_socket.recv(1024).decode("utf-8")
    print(f"Command received: {data}")

    if data == "open_notepad":
        import os
        os.system("notepad.exe")  # test

    client_socket.send(f"Command '{data}' executed".encode("utf-8"))
    client_socket.close()
