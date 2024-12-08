#!/usr/bin/python3

# progam menghitung luas lingkaran
# rumus lingkaran = phi X r X r


def luas_lingkaran(r: int) -> float:
    return 3.14 * (r * r)


r = int(input("Masukkan jari-jari lingkaran: "))
Luas = luas_lingkaran(r)

print(f"Luas lingkaran adalah {Luas}")
