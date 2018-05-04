# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://github.com/xieqilu/Qilu-leetcode/blob/master/B219.GetSExpressionBT.cs
#* Change C# to Python.

ALPHABET_CNT = 26

def get_char_to_index(ch):
    return ord(ch) - ord("A")

def get_index_to_char(index):
    return chr(index + ord("A"))

def get_child_node(index, root_index, matrix):
    for i in range(index, ALPHABET_CNT):
        if matrix[root_index][i]:
            return (get_sexpression(get_index_to_char(i), matrix), i+1)
    return ("", 0)

def get_sexpression(root, matrix):
    root_index = get_char_to_index(root)

    left, index = get_child_node(0, root_index, matrix)
    right, _ = get_child_node(index, root_index, matrix)

    return "(%s%s%s)" % (root, left, right)

def is_cycle(node, matrix, visited_matrix):
    node_index = get_char_to_index(node)

    if visited_matrix[node_index]:
        return True

    visited_matrix[node_index] = True
    for i in range(ALPHABET_CNT):
        if matrix[node_index][i] and is_cycle(get_index_to_char(i), matrix, visited_matrix):
            return True
    return False

def get_sexpression_bt(arg):
    if not arg:
        return "E5"

    matrix = [[False for x in range(ALPHABET_CNT)] for y in range(ALPHABET_CNT)]
    nodes = set()
    error = ""

    for node, child in arg:
        x = get_char_to_index(node)
        y = get_char_to_index(child)

        if matrix[x][y]:
            error = "E2"

        matrix[x][y] = True
        nodes.add(node)
        nodes.add(child)

    for i in range(ALPHABET_CNT):
        count = 0

        for j in range(ALPHABET_CNT):
            if matrix[i][j]:
                count += 1

        if count > 2:
            error = "E1"

    if error != "":
        return error

    root = ""
    root_count = 0
    for node in nodes:
        node_index = get_char_to_index(node)
        for i in range(ALPHABET_CNT):
            if matrix[i][node_index]:
                break

            if i == ALPHABET_CNT-1:
                root_count += 1
                root = node

                visited_matrix = [False for x in range(ALPHABET_CNT)]
                if is_cycle(node, matrix, visited_matrix):
                    return "E3"

    if root_count == 0:
        return "E3"
    elif root_count > 1:
        return "E4"
    elif root == "":
        return "E5"

    return get_sexpression(root, matrix)


if __name__ == "__main__":
    test_arg = [[("B","D"), ("D","E"), ("A","B"), ("C","F"), ("E","G"), ("A","C"), ("A", "K")],
                [("B","D"), ("D","E"), ("A","B"), ("C","F"), ("E","G"), ("A","C"), ("E","G")],
                [("A","B"), ("A","C"), ("B","D"), ("D","C")],
                [("A","B"), ("A","C"), ("B","G"), ("C","H"), ("E", "F"), ("B","D"),("C","E"), ("K","B"), ("K","C")],
                [],
                [("B","A"), ("B","C"), ("A","D")],
                [("B","D"), ("D","E"), ("A","B"), ("C","F"), ("E","G"), ("A","C")],
                [("A","B"), ("A","C"), ("B","G"), ("C","H"), ("E", "F"), ("B","D"),("C","E")]]

    for arg in test_arg:
        print (get_sexpression_bt(arg))
