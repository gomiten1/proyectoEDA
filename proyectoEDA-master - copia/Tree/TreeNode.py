class TreeNode:
    def __init__(self, key, value=0, name=""):
        self.right = None
        self.left = None
        self.key = key

        #self.value = value
        #self.name = name

    def __str__(self):
        return str(self.key)
    
