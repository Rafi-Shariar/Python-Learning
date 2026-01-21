str1 = "this is string1"
str2 = 'string2'
str3 = """this is string 3"""

# print(str2)
# print(len(str1))
# print(str2[3])

print("Slice str2 : ", str2[2:5])

# python supports -ev indexing. Example : Apple -> -5 -4 -3 -2 -1
print("-ev Indexing slice: ", str2[-4:-1])

#string functions
print(str2.endswith("2"))
print(str2.capitalize())
print(str2.replace('i','X'))
print(str2.find("s"))
print(str3.count("i"))

# f string
price = 59
txt = f"The price is {price} $"
print(price)

