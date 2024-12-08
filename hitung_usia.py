#!/usr/bin/python3
try:
    tahun_sekarang = int(input("Masukkan tahun sekarang: "))
    tahun_lahir = int(input("Masukkan tahun lahir: "))

    usia = tahun_sekarang - tahun_lahir

    print(f"Usia Anda sekarang adalah {usia} tahun.")
except ValueError:
    print("Pastikan tahun yang anda masukkan berupa angka")
