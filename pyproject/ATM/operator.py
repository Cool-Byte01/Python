#!/usr/bin/env python3

data_pengguna = []


def buat_akun(nama: str, no_rek: int, pin: int, saldo: int):
    pengguna = {"nama": nama, "no_rekening": no_rek, "pin": pin, "saldo": saldo}
    data_pengguna.append(pengguna)
    print(f"Selamat {pengguna['nama']} berhasil ditambahkan!")


def cek_saldo():
    pass


def tambah_saldo():
    pass


buat_akun("Andi", 9379, 1234, 5000)
