class TreeNode:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(TreeNode(name))

    def dft(self, array):
        visited = set()
        visited.add(self.children[0])
        for child in self.children[1:]:
            if child not in visited:
                array.append(child)
                self.dft(array)
                print(array)
        return array
