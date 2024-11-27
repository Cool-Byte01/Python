# str() digunakan untuk membuat objek / mengkonversi objek ke string.
# contoh str
a = "aku belajar koding"  # <- str

# int ke str
x = 10  # <- int o: 10
str(x)  # <- str o: '10'

# list ke str dsb.
y = [1, 2, 3, 4, 5]
str(y)

# repr untuk memberikan representasi objek dgn str
# contoh perbedaan str dan repr
import datetime

today = datetime.datetime.now()

my_repr = repr(today)
print(f"repr: {my_repr}\n")

my_str = str(today)
print(f"string: {my_str}")
