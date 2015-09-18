class Node:
    def __init__(self, p, val):
        self.left = None
        self.right = None
        self.value = val
        self.parent = p

        def __lt__(self, n2):
            return self.value < n2.value

        def __gt__(self, n2):
            return self.value > n2.value

        def __eq__(self, n2):
            return self.value == n2.value

        def __ne__(self, n2):
            return self.value != n2.value

        def __ge__(self, n2):
            return self.value >= n2.value

        def __le__(self, n2):
            return self.value <= n2.value

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def treeSearch(x, k):
        if x.value == k or x == None:
            return x
        if k < x.value:
            return treeSearch(x.left, k)
        else:
            return treeSearch(x.right, k)

    def InorderTreeWalk(self, x):
        if x == None:
            return
        self.InorderTreeWalk(x.left)
        print(x.value)
        self.InorderTreeWalk(x.right)

    def IterativeTreeSearch(self, x, k):
        while x != None and k != x.value:
            if k < x.value:
                x = x.left
            else:
                x = x.right
        return x

    def TreeInsert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.value <= y.value:
            y.left = z
        else:
            y.right = z

    def Transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.p.right = v
        if v != None:
            v.parent = u.parent

    def TreeDelete(self, z):
        if z.left == None:
            self.Transplant(z, z.right)
        elif z.right == None:
            self.Transplant(z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            if y.parent != z:
                self.Transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.Transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def TreeMinimum(self, x):
        while(x.left != None):
            x = x.left
        return x

    def __str__(self):
        self.InorderTreeWalk(self.root)
        return ""
