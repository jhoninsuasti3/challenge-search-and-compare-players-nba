my_list = [ 2, 3, 5, 2, 3, 6]
my_target = 5

print(f"Find pairs in {my_list} that sum up to {my_target}")

d = {}  # use a dictionary

result = []

for i in range(len(my_list)):

    if my_target - my_list[i] in d.keys():
        result.append((my_list[d[my_target - my_list[i]]], my_list[i]))
    d[my_list[i]] = i

print(f"results: {result}")