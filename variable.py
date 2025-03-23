# Variable Python
# Tidak ada konsep "Hoisting" jadinya variable dibaca dari atas sampai bawah (Hierarki)

price = 1000
print("starting price :", price)

discount = 0.5
print("discount :", discount)

price = price * discount
print("after discount price :", price)

product_name = "Mouse Gaming"
print("product name :", product_name)

is_discount = True
print("is discount? ", is_discount)