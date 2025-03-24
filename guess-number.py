chance = 3
answer = 7
index = 1

while index <= chance:
    user_guest = int(input("Masukkan Angka Tebakan 1 - 10 : "))
    if user_guest == answer:
        print("Selamat, Jawaban anda benar!")
        break
    else:
        print("Jawaban anda masih salah, coba lagi!")
        index += 1

if(index >= chance):
    print("Maaf, kesempatan anda habis, coba lagi!")
else:
    print("Terimakasih sudah bermain!")
