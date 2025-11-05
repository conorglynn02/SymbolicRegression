from tree.tree_node import TreeNode

class Tree:
    def __init__(self, node_value=None, function_string: str | None = None):
        self.root = TreeNode(node_value)
        self.function_string = function_string
        if function_string is not None:
            self.create_from_function_string(function_string)

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
        pass

    def full(self, max_height: int):
        pass
