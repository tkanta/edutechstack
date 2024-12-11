set_A = {1, 1, 2, 3, 4}
set_B = {2, 3, 3, 4, 5}

set_union = set_A.union(set_B)
set_intersection = set_A.intersection(set_B)
set_diff = set_A.difference(set_B)
set_sym_diff = set_A.symmetric_difference(set_B)

print("set union :", set_union)
print("set intersection :", set_intersection)
print("set difference :", set_diff)
print("set symmetric difference :", set_sym_diff)