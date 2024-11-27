# Float dan complex digunakan untuk konversi

# Template:
# float(number=0.0)
# complex(real=0, imag=0)
# complex(string)

# --- Float ---
# float(number=0.0)
# float() digunakan untuk mengkonversi angka atau string(numerik)
# ke bilangan floating-point.
print("Float\n")
print(float())  # jika argumen kosong akan mengembalikan 0.0(default)

print(float(42))  # mengembalikan floating-point 42.0
print(float("42\n"))  # string yg valid(numerik)

# print(float("one")) <- error karena bukan string numerik
print("\n")

# --- Complex ---
# complex() digunakan untuk mengkonversi angka atau string ke bilangan complex.

# --- Bilangan Complex dengan argumen real dan imag ---
# Template: complex(real=0, imag=0) <- ini mengambil dua argumen
# real = bilangan ril(asli)
# imag = bilangan imajiner dari angka tsb
print("Complex dua argumen\n")
print(complex(4, 2j))
# j digunakan untuk merepresentasikan bilangan imajiner di python

print(complex(0, 1j))
print(complex(3.14, -2.75j))
print("\n")

# --- Bilangan Complex dengan argumen string(numerik) ---
# Template: complex("string") <- ini hanya mengambil satu argumen
print("Complex saru argumen\n")
print(complex("3+2j"))
# jika mengunakan string sbg argumen:
# 1. String harus berupa bilangan ril, tanda dan bilangan imajiner
# 2. Bilangan harus mengunakan string numerik
# 3. Tidak boleh ada spasi atau tanda yg memisahkan didalam argumen

print(complex("5+2j"))
print(complex("1+0j"))
print(complex("1j"))
print(complex("2.45-2.12j"))
