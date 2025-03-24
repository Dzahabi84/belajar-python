# While

message = input("Masukkan pesan : ")
total_loop = int(input("Masukkan jumlah pengulangan : "))
index = 1

print("Mulai")

while index <= total_loop:
    print(f'{message} ke {index}')
    index += 1

print("Finish")