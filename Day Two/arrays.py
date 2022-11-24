new_list = [1, 2, 3]
result = new_list[1]

if 1 in new_list:
    print("Found")
print(result)
for n in new_list:
    if n == 2:
        print("Found")
        break

new_list.append(4)
new_list.pop()
print(new_list)