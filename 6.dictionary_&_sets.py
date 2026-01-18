#dictionary: similar to maps. store values of key:value.
#unorder, mutable & dont allow duplicate

info = {
    "name" : "Rafi shariar",
    "age" : 21,
    "phone" : "01823234",
    "married" : True,
    "marks" : [12,2,3,4,55,6]
}

print(info)
print( info["name"])

#set: immutable, no duplicate, unordered
thisset = {"apple", "orange", "apple"}
print(thisset)

set2 = {1, True, "Rafi"}
print(set2)