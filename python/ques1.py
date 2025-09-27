list = [4,2,45,2,3,2,3,4,8]

# for i in range(1 , 11) : 
#     list.append(i);

# print(list)


min = list[0] 
max = list[0]
for i in list : 
    if i < min : 
        min = i
    if i > max : 
        max = i

print(f"Min : {min} , Max : {max}")

reversed = list[::-1]
print(reversed)

hash = [] 
for i in list : 
    if i not in hash : 
        hash.append(i)
    else : 
        list.remove(i)

print("Unique list : " , list)

