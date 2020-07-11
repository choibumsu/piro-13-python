import this
print()


# string
ex_str = "Hi I'm Bumsu, I'm a frontend developer"

# find, index
find_idx = ex_str.find("Bumsu")
index_idx = ex_str.index("Bumsu")
print(find_idx, index_idx)

try:
    find_idx = ex_str.find("Piro")
    index_idx = ex_str.index("Piro")
    print(find_idx, index_idx, "\n")
except Exception as e:
    print(e, "\n")

# split
splited_list = ex_str.split(" ")
print(splited_list, "\n")

# join
joined_str = "%20".join(splited_list)
print(joined_str, "\n")

# replace
replaced_str = ex_str.replace("frontend", "backend")
print(replaced_str, "\n")

# strip
dummy_str = "         hi hi                      "
stripped_str = dummy_str.strip()
print(stripped_str)
print(len(stripped_str), "\n")

# f string
name = "bumsu"
job = "developer"
print(f"Hello I'm {name}, I'm a {job}\n")

# ------

# list
ex_list = [1, 2, 3, 4, 5, 6, 7]

# extend
another_list = [8, 9, 10]
ex_list.extend(another_list)
print(ex_list, "\n")


# ------

# Dictionary
ex_dic = {
    "name": "bumsu",
    "age": 25,
    "job": "developer"
}

# keys
ex_keys = list(ex_dic.keys())
print(ex_keys)

# values
ex_values = list(ex_dic.values())
print(ex_values)

# items
ex_items = list(ex_dic.items())
print(ex_items, "\n")

# ------

# lambda, map, filter

# lambda
ex_lambda = (lambda x: x + 10)
print(ex_lambda(1))
print(ex_lambda(2))
print(ex_lambda(3), "\n")

# map(function, list)
numbers = [1, 2, 3, 4, 5]
ex_map_1 = list(map(str, numbers))
print("map 1", ex_map_1)


def add10(x):
    return x + 10


ex_map_2 = list(map(add10, numbers))
print("map 2", ex_map_2)

ex_map_3 = list(map(lambda x: x + 10, numbers))
print("map 3", ex_map_3)

ex_map_4 = []
for number in numbers:
    # result = (lambda x: x + 10)(number)
    result = number + 10
    ex_map_4.append(result)
print("map 4", ex_map_4, "\n")


# filter(function, list)
ex_filter_1 = list(filter(lambda x: x > 3, numbers))
print("filter 1", ex_filter_1)

ex_filter_2 = []
for number in numbers:
    if number > 3:
        ex_filter_2.append(number)
print("filter 2", ex_filter_2, "\n")
