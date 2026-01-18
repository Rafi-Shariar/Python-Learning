#while
i = 0
while i < 6:
    print(i)
    if(i == 3):
        break
    i+=1


# for
print("For Loop results:")
for i in range(0,3):
    print(i)


fruits = ["apple", "banana", "orage"]
for i in fruits:
    print(i)
    if(i == "banana"):
        break


for i in range(3):
    print("hellow-", i)
else:
    print("Done!")