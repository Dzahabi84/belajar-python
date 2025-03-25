si_abdul = ["Abdullah", 32, "Islam", True]
print(si_abdul)
print(si_abdul[3])
print(si_abdul[2:3])
print(si_abdul[-2])

for item in si_abdul:
    print(item)

# List Method And Function
numbers = [200, 35, 70, 80]
print(numbers)

numbers.append(35)
print(numbers)

numbers.insert(3, 300)
print(numbers)

numbers.pop(2)
print(numbers)

numbers.remove(35)
print(numbers)

numbers.sort()
print(numbers)

sum_number = sum(numbers)
max_number = max(numbers)
print(sum_number)
print(max_number)