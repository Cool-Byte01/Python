#!/usr/bin/python3
import os


# fungsi untuk menampilkan daftar file
def list_file_and_dir(directory):
    """
    Program sederhana untuk menampilkan file dan folder.
    Pada input "Masukkan path direktori" masukkan path yanglengkap    lengkap. contohnya: "/data/data/com.termux/files/home" atau
    tekan enter untuk menampilkan file dan direktori pada folder
    saai ini.

    Penjelasan method yang digunakan:
    - os.listdir() untuk mengambil semua nama file dan direktori.
    - os.isfile() dan os.isdir() untuk mengecek file atau folder
    menggunakan path lengkap.
    - os.path.join() untuk membuat path lengkap.
    - os.getcwd() untuk mengambil direktori saat ini.
    """
    try:
        # mendapatkan daftar ssmua file dan folder
        items = os.listdir(directory)
        print(f"Daftar file dan folder di directory: {directory}")
        for item in items:
            # menggabungkan path lengkap
            full_path = os.path.join(directory, item)

            if os.path.isfile(full_path):
                print(f"File: {item}")
            elif os.path.isdir(full_path):
                print(f"Folder: {item}")
    except FileNotFoundError:
        print("Direktori tidak ditemukan.")
    except PermissionError:
        print("Tidak memiliki izin untuk mengakses direktori ini.")


# direktori target
target_direktori = (
    input("Masukkan path direktori(kosongkan untuk durektori saat ini): ")
    or os.getcwd()
)

# memanggil fungsi
list_file_and_dir(target_direktori)
