class Tree:
    def __init__(self, data) -> None:
        """
        Initializes a Tree node with the given data.
        
        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        """
        Adds a child node to the current node.
        
        Args:
            child: The child node to be added.
        """
        child.parent = self
        self.children.append(child)
    
    def get_level(self) -> int:
        """
        Returns the level of the current node in the tree.
        
        Returns:
            int: The level of the current node.
        """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        """
        Prints the tree structure starting from the current node.
        """
        level = ' ' * self.get_level() * 2
        prefix = level + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

# Example Usage

tree = Tree("Electronics")
laptop = Tree("Laptops")
mobiles = Tree("Mobiles")
tablets = Tree("Tablets")

laptop.add_child(Tree("HP"))
laptop.add_child(Tree("ASUS"))
laptop.add_child(Tree("Lenovo"))

mobiles.add_child(Tree("Lava"))
mobiles.add_child(Tree("Lenovo"))
mobiles.add_child(Tree("MicroMax"))
mobiles.add_child(Tree("Redmi"))
mobiles.add_child(Tree("Asus"))
mobiles.add_child(Tree("Realme"))
mobiles.add_child(Tree("Iqoo"))

tablets.add_child(Tree("Apple Ipad"))

tree.add_child(laptop)
tree.add_child(mobiles)
tree.add_child(tablets)

tree.print_tree()