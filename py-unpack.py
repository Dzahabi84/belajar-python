with_list = [1,2,3,4,5,6]
with_tuple = (1,2,3,4,5,6)

x, y, _, *z = with_list
print(x)
print(y)
print(z)
print("---------")
a, b, _, *c = with_tuple
print(a)
print(b)
print(c)
print("---------")