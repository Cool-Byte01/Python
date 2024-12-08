import socket

targetIP = "127.0.0.1"
targetPort = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pesan = "Halo, Testing doang kok"
client.sendto(pesan.encode(), (targetIP, targetPort))

data, addr = client.recvfrom(4096)
print(f"Pesan dari server:\n, {data}")

client.close()
