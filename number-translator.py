numbers = input("Masukkan angka : ")

numbers_mapping = {
    "1": "Satu",
    "2": "Dua",
    "3": "Tiga",
    "4": "Empat",
    "5": "Lima",
    "6": "Enam",
    "7": "Tujuh",
    "8": "Delapan",
    "9": "Sembilan",
    "10": "Sepuluh",
}

output = ""

for n in numbers:
    number_translate = numbers_mapping.get(n, "Invalid")
    output = output + number_translate + " "

print(output)