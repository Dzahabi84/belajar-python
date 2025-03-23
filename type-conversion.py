# Type Conversion (Menentukan Umur Dari Tanggal Lahir)

birth_date = int(input("Masukkan Tanggal Lahir : "))
print("birth_date type : ", type(birth_date))

age = 2025 - birth_date
print("age type : ", type(age))

print("Umur kamu di tahun 2025 adalah : " + str(age))
print("after age type : ", type(str(age)))