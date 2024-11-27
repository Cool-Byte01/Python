# divmod() : Untuk menemukan hasil bagi dan sisa bagi.
# sama dengan (a // b, a % b) / (q, a % b), q = a / b
print(divmod(8, 4))
print(divmod(6.5, 3.5))

# studi kasus : mengambil nilai milidetik,
# dan mengembalikan string dengan format 00:00:00


def hh_mm_ss(milisecond):
    second = round(milisecond / 1000)
    minutes, second = divmod(second, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{second:02d}"


print(hh_mm_ss(20000))
