# min dan max digunakan untuk mencari nilai
# terkecil dan terbesar dalam suaru iterabel.

print(max([1, 2, 3, 4, 5]))
print(min([1, 2, 3, 4, 5]))

print(max(1, 2, 3, 4, 5))
print(min(1, 2, 3, 4, 5))

# min(iterable, *[, default, key])
# max(iterable, *[, default, key])

# - default : Mengembalikan nilai jika input kosong
# - key : Menerima argumen fungsi tunggal untuk
#         menyesuaikan kriteria perbandingan

print(max([], default=0))
print(min([], default=0))

print(max([-2, 3, 4, -5, 1], key=abs))
print(min([-2, 3, 4, -5, 1], key=abs))
