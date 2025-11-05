class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.operations_set = set(['+', '-', '*', '/'])

    def add_child(self, child_node):
        if not self.left:
            self.left = child_node
        elif not self.right:
            self.right = child_node
        else:
            raise ValueError("Attempting to have more than two children.")

    def remove_child(self, child_node):
        if self.left == child_node:
            self.left = None
        elif self.right == child_node:
            self.right = None
        else:
            raise ValueError("Child not found.")

    def is_leaf(self) -> bool:
        return not self.left and not self.right

    def evaluate(self) -> float:
        # might need to call my in order search methods
        return self._inorder_evaluate_helper(self, self)

    def _inorder_evaluate_helper(self, node) -> float:
        if node is not None:
            left = self._inorder_evaluate_helper(node.left)
            right = self._inorder_evaluate_helper(node.right)
            if node.value in self.operations_set:
                # need to perform the operation on the left and right child values, but they may be further operations themselves
                if node.value == '+':
                    return left + right
                elif node.value == '-':
                    return left - right
                elif node.value == '*':
                    return left * right
                elif node.value == '/':
                    return left / right if right != 0 else 0  # avoid division by zero
            else:
                return node.value  # base case: leaf node with a numeric value
        else:
            return 0
