# int() : tipe data python yang mewakili bilangan bulat

# jika tanpa argumen mengembalikan 0.
print(int())  # 0

# jika floating point int akan menghapus
# angka dibelakang titik
print(int(42.42))  # 42

# jika string, int juga akan mengembalikan bilangan bulat
# ketika string tsb mewakili angka yang valid.
print(int("40"))  # 40

# contoh yang tidak valid

# print(int("40.20"))  <-- ini error
# print(int("one"))   <--- itu juga error

# ValueError: invalid literal for int() with base 10: '40.20'

# int() untuk mengkonversi strig menjadi biner,
# oktal dan hexadecimal

# biner
print(int("0b10", base=2))
# oktal
print(int("0o10", base=8))
# hexadecimal
print(int("0x10", base=16))


# ---------- bin() --------------
# bin() : untuk mengkonversi integer ke biner
print(bin(42))

# ---------- oct() --------------
# oct() : untuk mengkonversi integer ke oktal
print(oct(42))

# ---------- hex() --------------
# hex() : untuk mengkonversi integer ke hexadecimal
print(hex(42))
