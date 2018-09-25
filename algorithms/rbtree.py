"""An implementation of red-black trees, based on the description in
Introduction to Algorithms (Cormen, Leiserson, Rivest), Chapter 14.

Danny Yoo (dyoo@hkn.eecs.berkeley.edu)
"""

RED = "RED"
BLACK = "BLACK"

class NilNode(object):
    def __init__(self):
        self.color = BLACK

NIL = NilNode()

class Node(object):
    def __init__(self, key, color=RED, left=NIL, right=NIL, p=NIL):
        assert color in (RED, BLACK)
        self.color, self.key, self.left, self.right, self.p = (
            color, key, left, right, p)

class Tree(object):
    def __init__(self, root=NIL):
        self.root = root


def left_rotate(T, x):
    assert (x.right != NIL)
    y = x.right
    x.right = y.left
    if y.left != NIL:
        y.left.p = x
    y.p = x.p
    if x.p == NIL:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y


def right_rotate(T, x):
    assert (x.left != NIL)
    y = x.left
    x.left = y.right
    if y.right != NIL:
        y.right.p = x
    y.p = x.p
    if x.p == NIL:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y



def tree_insert(tree, z):
    y = NIL
    x = tree.root
    while x != NIL:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == NIL:
        tree.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def rb_insert(tree, x):
    tree_insert(tree, x)
    x.color = RED
    while x != tree.root and x.p.color == RED:
        if x.p == x.p.p.left:
            y = x.p.p.right
            if y.color == RED:
                x.p.color = BLACK
                y.color = BLACK
                x.p.p.color = RED
                x = x.p.p
            else:
                if x == x.p.right:
                    x = x.p
                    left_rotate(tree, x)
                x.p.color = BLACK
                x.p.p.color = RED
                right_rotate(tree, x.p.p)
        else:
            y = x.p.p.left
            if y.color == RED:
                x.p.color = BLACK
                y.color = BLACK
                x.p.p.color = RED
                x = x.p.p
            else:
                if x == x.p.left:
                    x = x.p
                    right_rotate(tree, x)
                x.p.color = BLACK
                x.p.p.color = RED
                left_rotate(tree, x.p.p)
    tree.root.color = BLACK


def tree_minimum(x):
    while x.left != NIL:
        x = x.left
    return x


def tree_maximum(x):
    while x.right != NIL:
        x = x.right
    return x


def tree_successor(x):
    if x.right != NIL:
        return tree_minimum(x.right)
    y = x.p
    while y != NIL and x == y.right:
        x = y
        y = y.p
    return y


def tree_predecessor(x):
    if x.left != NIL:
        return tree_maximum(x.left)
    y = x.p
    while y != NIL and x == y.left:
        x =y
        y = y.p
    return y


def tree_height(node):
    if node == NIL: return 0
    return max(1 + tree_height(node.left), 1 + tree_height(node.right))


def tree_count_internal(node):
    if node == NIL: return 0
    return 1 + tree_count_internal(node.left) + tree_count_internal(node.right)
