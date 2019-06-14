import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# original, 6.4s
# O(1 + n * n + 1 + 1) -> O(n^2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# 1st pass, 1.3s
# O(1 + n * n + 1) -> O(n^2)
# Python's `in` operator is more efficient than `for` loop but still O(n)
# duplicates = []
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

# 2nd pass with hash table, 0.004s
# O(n + n * 1) -> O(2n) -> O(n)
lookup = {name: True for name in names_1}
duplicates = [n for n in names_2 if n in lookup]

# 3rd pass with BST, 0.2s
# O(1 + n * log n + n * log n) -> O(2n log n) -> O(n log n)
# lookup = BinarySearchTree('init')
# for name in names_1:
#     lookup.insert(name)
# duplicates = [n for n in names_2 if lookup.contains(n)]


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
