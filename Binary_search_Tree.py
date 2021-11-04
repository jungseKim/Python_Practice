class Node:
    def __init__(s, data, left=None, rigth=None):
        s.data = data
        s.left = left
        s.rigth = rigth


class NodeAlll:
    def __init__(s):
        s.root = None

    def input(s, node, data):
        if s.root == None:
            return Node(data)
        if node.data == data:
            return node
        if node.data > data:
            node.left = s.input(node.left, data)
        else:
            node.rigth = s.input(node.rigth, data)
        return node


na = NodeAlll()
temp = [1, 24, 5, 5]

for i in temp:
    na.root = na.input(na.root, i)


def fc(n):
    print(n.data)
    if(n.left):
        fc(n.left)
    if(n.rigth):
        fc(n.rigth)


fc(na.root)
