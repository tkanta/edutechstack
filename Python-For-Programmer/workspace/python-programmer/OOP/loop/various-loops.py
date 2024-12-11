# Float list iteration
# float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
#
# for i in range(0, len(float_list)):
#     float_list[i] = float_list[i] * 2
#
# print(float_list)

# for j in range(1, 11):
#     print(j)

# print("-------------------")
# num_list = list(range(5))
# for i in num_list:
#     if i == 3 or i == 6:
#         continue
#     print(i)

print("---------------")
list_no = list(range(5))
for i in list_no:
    for j in range(1, 3):
        if i != j:
            continue
        if i == j:
            break

    print(i,j)