import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8001))

server.listen()

try:
    while True:
        client, address = server.accept()
        data = client.recv(5000).decode()
        print(f"{data=}")

        # Response
        client.sendall(
            "HTTP/1.0 200 OK\r\n\r\n<html><body>hello</body></html>\r\n\r\n".encode()
        )
        client.shutdown(socket.SHUT_WR)


except Exception:
    server.close()