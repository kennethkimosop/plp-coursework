# 1. Create an empty list
my_list = list()

# 2. Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("After appending:", my_list)

# 3. Insert 15 at the second position (index 1, since indexing starts at 0)
my_list.insert(1, 15)
print("After inserting 15 at position 2:", my_list)

# 4. Extend with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# 5. Remove the last element
my_list.pop()
print("After removing last element:", my_list)

# 6. Sort the list in ascending order
my_list.sort()
print("After sorting:", my_list)

# 7. index of value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)
