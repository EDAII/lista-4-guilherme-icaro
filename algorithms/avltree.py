class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class AvlTree():
    def __init__(self, *arguments):
        self.node = None
        self.height = -1
        self.factor_balance = 0

        if len(arguments) == 1:
            for i in arguments[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def check_leaf(self):
        return (self.height == 0)

    def insert(self, value):

        tree = self.node

        new_node = Node(value)

        if tree == None:
            self.node = new_node
            self.node.left = AvlTree()
            self.node.right = AvlTree()
            # print("Valor inserido com sucesso!")
        elif value < tree.value:
            self.node.left.insert(value)
        elif value > tree.value:
            self.node.right.insert(value)
        else:
            pass
            # print("O valor já pertence a árvore.")

        self.rebalance()

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.left_rotation()
                    self.update_heights()
                    self.update_balances()
                self.right_rotation()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.right_rotation()
                    self.update_heights()
                    self.update_balances()
                self.left_rotation()
                self.update_heights()
                self.update_balances()

    def right_rotation(self):

        # print("Realiza rotação para a direita com o valor {}!".format(self.node.value))
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def left_rotation(self):

        # print("Realiza rotação para esquerda com o valor {}!".format(self.node.value))
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, value):
        if self.node != None:
            if self.node.value == value:
                # print("Removendo o valor {}".format(value))
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node
                else: # pior caso: quando possui dois filhos -> deve-se encontrar o sucessor lógico para troca
                    replacement = self.logical_successor(self.node)
                    if replacement != None:
                        self.node.value = replacement.value

                        # Com o elemento trocado, já pode-se realizar a remoção
                        self.node.right.delete(replacement.value)

                # Rebalancear a árvore
                self.rebalance()
                return
            elif value < self.node.value:
                self.node.left.delete(value)
            elif value > self.node.value:
                self.node.right.delete(value)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        node = node.right.node
        if node != None:
            while node.left != None:
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # Deve sempre conferir se a árvore está balanceada
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.value)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist
