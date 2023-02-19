"""import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect(("example.com", 80))

# request
cmd = "GET http://example.com/index.html HTTP/1.0\r\n\r\n".encode()

client.send(cmd)

while True:
    data = client.recv(1024)
    if len(data) < 1:
        break
    print(data.decode(), end="")

client.close()

import requests
res = requests.get("http://www.example.com/index.html")
"""
import httpx
res = httpx.get("http://localhost:9001")

print(res.status_code)
print(res.headers)
#print(res.content)