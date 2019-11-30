tree = [int(x) for x in open(r"..\..\input.txt").read().split(" ")]
metadata = 0
nodes = {}

def traverse_tree(tree, position):
    number_kids = tree[position]
    number_metadata = tree[position+1]
    position += 2
    global metadata
    child_values = [None]*number_kids

    for i in range(number_kids):
    	position, child_values[i-1] = traverse_tree(tree, position)

    branch_value = 0
    for i in range(number_metadata):
    	metadata += tree[position]
    	branch_value += tree[position]
    	position += 1

    child_values = branch_value if number_kids == 0 else child_values
    return position, child_values

print(traverse_tree(tree, 0)[1])