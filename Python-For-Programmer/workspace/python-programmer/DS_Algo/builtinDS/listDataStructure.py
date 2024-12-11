num_seq = range(0, 10)  # A sequence from 0 to 9
num_list = list(num_seq)  # The list() method casts the sequence into a list
print(num_seq)
print(num_list)

num_seq = range(3, 20, 3)  # A sequence from 3 to 19 with a step of 3
print(list(num_seq))

# nested list
world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
print(world_cup_winners)

# merge list
part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)


def merge_sorted_lists(list1, list2):
    merged_list = []

    # Merge the two lists
    merged_list = list1 + list2
    # Append remaining elements (if any)

    return merged_list


# Test the function
list1 = [4, 6, 8, 10]
list2 = [3, 7, 11, 12]
print(merge_sorted_lists(list1, list2))  # Output: [3, 4, 6, 7, 8, 10, 11, 12]