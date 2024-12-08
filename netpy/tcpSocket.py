import socket

targetHost = "dpr.go.id"
targetPort = 80

# membuat socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((targetHost, targetPort))

client.send(b"GET / HTTP/1.1\r\nHost: dpr.go.id\r\n\r\n")

# menangkap respon
respon = client.recv(4096)
print(respon.decode())

client.close()
