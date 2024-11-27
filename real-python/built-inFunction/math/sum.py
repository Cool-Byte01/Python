# sum() : digunakan untuk menjumlahkan serangkaian nilai
# sum(iterabel[, start=0])

# iterabel = argumen yg dibutuhkan yg dpt menampung literasi python.
# start(opsional) = argumen opsional untuk menentukan nilai awal.

print(sum([1, 2, 3, 4, 5]))  # = 15

# dgn argumen start
# keyword argumen
print(sum([1, 2, 3, 4, 5], start=5))  # = 20

# posisional argumen
print(sum([1, 2, 3, 4, 5], 5))  # = 20

# sum untuk menggabungkan list atau tuple,
# caranya beri argumen start dengan tipe data yang ingin di gabungkan
# ini berfungsi tpi tidak efektif

# menggunakan list
use_list = [1, 2, 3], [4, 5, 6]
print(sum(use_list, start=[]))

# menggunakan tuple
use_tuple = (1, 2, 3, 4), (5, 6, 7, 8)
print(sum(use_tuple, start=()))


# studi kasus : mencari nilai rata-rata dengan sum


def rata_rata(nilai):
    try:
        return sum(nilai) / len(nilai)
    except ZeroDivisionError:
        raise ValueError("Fungsi ini eror karena anda membagi dengan 0") from None


print(rata_rata((65, 70, 75, 60, 85, 80)))
