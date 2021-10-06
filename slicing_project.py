import random

num_list = []
num_66 = False

for num in range(12):
    num_list.append(random.randint(50,80))

num_list.sort()

for i in num_list:
    print(i, end=" ")
    if i == 66:
        num_66 = True
print()

if num_66:
    print("66 is in the list.")

print(f"max num is: {max(num_list)}")
print(f"min num is: {min(num_list)}")

slice_indexes = num_list[4:9]
while 

total = sum(slice_indexes)
print(total)

# print(num_list)