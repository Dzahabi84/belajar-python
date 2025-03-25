# For In
name = "Agung"
list_makanan = ["Apel", "Jeruk", "Mangga"]
for item in name:
    print(item)

for item in range(1,10,2):
    print(item)

for item in list_makanan:
    print(item)

# While

message = input("Masukkan pesan : ")
total_loop = int(input("Masukkan jumlah pengulangan : "))
index = 1

print("Mulai")

while index <= total_loop:
    print(f'{message} ke {index}')
    index += 1

print("Finish")