# pow() : Mengambil angka dan menaikkannya ke pangkat tertentu.
# pow(base, exp[, mod=None]), mod = modulus(%). sisa bagi
# pow(2, 8) = 2 ** 8
print(pow(2, 4))

import timeit  # untuk menghitung waktu komputasi

base = 2
exp = 1000000
mod = 1000000

# menggunakan argumen mod
x = timeit.timeit("pow(base, exp, mod)", globals=globals(), number=10) * 1000

print(f"x dengan argumen mod: {x}")

# menggunakan modulus
x = timeit.timeit("pow(base, exp) % mod", globals=globals(), number=10) * 1000

print(f"x dengan operator modulus: {x}")
