import os
import random


def tebak_angka(angka_awal: int, angka_akhir: int):
    """
    Game tebak angka sederhana.
    Secara default 1-10
    """
    angka_rahasia = random.randint(angka_awal, angka_akhir)
    while True:
        try:
            tebakan = int(input("Masukkan Tebakan: "))
            if tebakan > angka_rahasia:
                print("Tebakanmu Terlalu Besar")
            elif tebakan < angka_rahasia:
                print("Tebakanmu Terlalu Kecil")
            else:
                print("Tebakanmu Benar\n\n")
                input("Tekan enter untuk mekanjutkan -> ")
                # main_lagi = input("Mau main lagi?(y/n): ").lower()
                # if main_lagi == "n":
                break
        except ValueError:
            print("Pastikan angka yang anda masukkan benar!")


# Menu
while True:
    nama_os = os.name
    match nama_os:
        case "posix":
            os.system("clear")

    print("""
    ========== Menu ==========
    1. Main
    2. Keluar
    """)
    try:
        pilih = input("Masukkan pilihan anda(1/2): ")
        if pilih == "1":
            print("Pilih Jarak Angka Yang Ingin Ditebak")
            angka_awal = int(input("Masukkan angka awal: "))
            angka_akhir = int(input("Masukkan angka akhir: "))
            tebak_angka(angka_awal, angka_akhir)
        elif pilih == "2":
            input("Tekan enter untuk keluar -> ")
            break
    except ValueError:
        print("Pastikan angka yang anda masukkan benar!")
