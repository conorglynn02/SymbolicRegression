import random
from tree.tree_node import TreeNode

OPERATIONS = ['+', '-', '*', '/']
CONSTANTS = [0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
VARIABLES = ['x', 'y', 'z']
TERMINALS = VARIABLES * 2 + CONSTANTS

class Tree:
    def __init__(self, node_value=None):
        self.root = TreeNode(node_value)

    def to_string(self) -> str:
        return self._to_string_helper(self.root)
    
    def _to_string_helper(self, node: TreeNode) -> str:
        if node is None:
            return ""
        if node.is_leaf():
            return str(node.value)
        left_str = self._to_string_helper(node.left)
        right_str = self._to_string_helper(node.right)
        return f"({left_str}{node.value}{right_str})"

    def print_tree(self):
        print(self.to_string())

    def traverse_scott_depth_first(self) -> list:
        return []

    def traverse_scott_breadth_first(self) -> list:
        return []

    def traverse_scott_in_order(self) -> list:
        return []
    
    def generate_random_structure(self, max_height: int) -> list:
        if max_height <= 0:
            return []

    def grow(self, max_height: int):
        self.root = TreeNode(None)
        self._grow(self.root, 1, max_height)

    def _grow(self, node: TreeNode, current_height: int, max_height: int):
        if current_height < max_height and random.random() < 0.7:
                node.value = random.choice(OPERATIONS)
                node.left = TreeNode(None)
                node.right = TreeNode(None)
                self._grow(node.left, current_height + 1, max_height)
                self._grow(node.right, current_height + 1, max_height)
        else:
            node.value = random.choice(TERMINALS)

    def full(self, max_height: int):
        self.root = TreeNode(None)
        self._full(self.root, 1, max_height)

    def _full(self, node: TreeNode, current_height: int, max_height: int):
        if current_height < max_height:
            node.value = random.choice(OPERATIONS)
            node.left = TreeNode(None)
            node.right = TreeNode(None)
            self._full(node.left, current_height + 1, max_height)
            self._full(node.right, current_height + 1, max_height)
        else:
            node.value = random.choice(TERMINALS)
