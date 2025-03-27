# Error Handling
def double_number(number):
    return number * 2

try:
    input_number = input("Masukkan angka : ")
    result = double_number(int(input_number))
    print(result)
except:
    print("Anda memiliki kesalahan!")
