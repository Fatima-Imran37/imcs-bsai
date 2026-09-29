my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
smallest = my_list[0]
for i in my_list:
    if i < smallest:
        smallest = i 

print(smallest)