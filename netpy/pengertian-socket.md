# Pengertian Socket

Socket adalah penghubung antara dua aplikasi yang dapat
berkomunikasi satu sama lain(baik secara lokal pada satu mesin
atau jarak jauh antara dua mesin di lokasi terpisah).

Pada dasarnya, socket berfungsi sebagai tautan komunikasi
antara dua entitas, yaitu klien dan server. Server akan
memberikan informasi yang diminta oleh klien. Misalnya,
ketika kamu mengunjugi halaman ini, browser akan membuat 
socket dan terhubung ke server.

[sumber]([https://code.tutsplus.com/id/introduction-to-network-programming-in-python--cms-30459t](Source)
)

# Perbedaan Socket dan Port

1. Socket

Definisi: Socket adalah kombinasi dari alamat IP dan nomor port
yang digunakan untuk membentuk sebuah endpoint komunikasi. 
Dalam jaringan, socket memungkinkan dua perangkat saling
berkomunikasi, baik melalui protokol TCP maupun UDP.

Fungsi: Socket digunakan untuk mendirikan, mengelola, 
dan mengakhiri koneksi jaringan.

Jenis:
Socket TCP: Untuk komunikasi berbasis koneksi (connection-oriented), seperti transfer data menggunakan HTTP.
Socket UDP: Untuk komunikasi tanpa koneksi (connectionless), seperti streaming video atau game online.


Contoh: 192.168.1.1:80

Alamat IP: 192.168.1.1

Port: 80 (biasanya untuk HTTP)



2. Port

Definisi: Port adalah angka unik yang digunakan untuk mengidentifikasi proses atau layanan tertentu pada perangkat. Port menjadi bagian dari alamat socket untuk memastikan data diteruskan ke aplikasi atau layanan yang benar.

Fungsi: Port memisahkan komunikasi antara berbagai layanan di satu perangkat. Misalnya, web server menggunakan port 80, sedangkan server SSH menggunakan port 22.

Jenis:

Port Well-Known (0-1023): Digunakan oleh layanan standar seperti HTTP (80), HTTPS (443), dan FTP (21).

Port Registered (1024-49151): Digunakan oleh aplikasi tertentu yang terdaftar.

Port Dynamic/Private (49152-65535): Digunakan secara dinamis untuk komunikasi klien.


Contoh: 80, 22, 443.


Perbedaan Utama

Dengan kata lain, port adalah komponen dari socket, dan socket digunakan untuk mendirikan komunikasi antara perangkat dalam jaringan.

------------------------------
|Aspek    |Socket     |Port   |
|-----------------------------
|Definisi |kombinasi  |
|         |alamat ip  |
|         |dan port.  |
