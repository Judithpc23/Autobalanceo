class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class AVLTree:

    def __init__(self, root: "Node"):
        self.root = root


    def getHeight(self, node: "Node"):
        if node is None:
            return 0
        else:
            return max(self.getHeight(node.left), self.getHeight(node.right)) + 1


    def getBalance(self, node: "Node"):
        if node is None:
            return 0
        return self.getHeight(node.right) - self.getHeight(node.left)


    def rebalance(self, node: "Node"):
        if self.getBalance(node) > 1:
            if self.getBalance(node.right) >= 0:
                return self.rotate_left(node)
            else:
                return self.rotate_right_left(node)
        elif self.getBalance(node) < -1:
            if self.getBalance(node.left) <= 0:
                return self.rotate_right(node)
            else:
                return self.rotate_left_right(node)
        return node