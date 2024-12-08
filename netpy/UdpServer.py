import socket

localIP = "127.0.0.1"
localPort = 12345
buffer = 1024

serverUdp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverUdp.bind((localIP, localPort))
print("Server Up!")

while True:
    data = serverUdp.recvfrom(buffer)
    pesan = data[0]
    ip_addr = data[1]

    print(f"Pesan dari client: {pesan}")
    print(f"IP client: {ip_addr}")

    serverUdp.sendto(
        b"Berhasil tersambung ke server! Selamat Datang di UDP Server", ip_addr
    )
