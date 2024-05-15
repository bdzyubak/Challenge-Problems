# Implement the unique_names method. When passed two arrays of names, it will return an array containing the names that appear in either or both arrays.
#
# The returned array should have no duplicates.
#
# For example, calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']) should return an array containing Ava, Emma, Olivia, and Sophia in any order.


def unique_names(names1, names2):
    # Easiest
    return set(names1+names2)

# def unique_names(names1, names2):
#
#     # From scratch for practice
#     names1_unique = list()
#     for name in names1:
#         if name not in names1_unique:
#             names1_unique.append(name)
#     unique_names = names1_unique + [name for name in names2 if name not in names1]
#
#     return unique_names


names1 = ["Ava", "Emma", "Ava", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia
