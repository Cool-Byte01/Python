"""
bool() merepresentasikan nilai benar atau salah dari sebuah objek.
 beriku yg di kategorikan false:
 1. Konstanta yang didefinisikan sebagai salah: None dan False
 2. Nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0),Fraction(0, 1)
 3. Urutan dan koleksi kosong: '', (), [], {}, set(),range(0)
 Objek lainnya dianggap benar dalam Python. Objek kustom dianggap
 benar secara default kecuali jika objek tersebut menyediakan
 .__bool__() metode khusus yang mendefinisikan perilaku berbeda.
"""
