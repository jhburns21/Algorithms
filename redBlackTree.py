class RBNode:
    def __init__(self, p, val):
        self.left = None
        self.right = None
        self.value = val
        self.parent = p
        self.color = "red"

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

class RBTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

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

    def RBInsert(self, z):
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
        z.left = None
        z.right = None
        z.color = "red"
        self.RBInsertFix(z)

    def RBInsertFix(self, z):
        while z.parent.color == "red":
            if z.parent = z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.LeftRotate(z)
                z.parent.color = "black"
                z.parent.parent.color = "red"
                self.RightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == "red":
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.RightRotate(z)
                z.parent.color = "black"
                z.parent.parent.color = "red"
                self.LeftRotate(z.parent.parent)
        self.root.color = "black"

    def RBTransplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def TreeDelete(self, z):
        y = z
        yoc = y.color
        if z.left == None:
            x = z.right
            self.RBTransplant(z, z.right)
        elif z.right == None:
            x = z.left
            self.RBTransplant(z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            yoc = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.RBTransplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.RBTransplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if yoc == "black":
            self.RBDeleteFixup(x)

    def RBDeleteFixup(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.LeftRotate(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                elif w.right.color == "black":
                    w.left.color = "black"
                    w.color = "red"
                    self.RightRotate(w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = "black"
                w.right.color = "black"
                self.LeftRotate(x.parent)
                x = self.root
            else:
                w = x.parent.left
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.RightRotate(x.parent)
                    w = x.parent.left
                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.parent
                elif w.left.color == "black":
                    w.right.color = "black"
                    w.color = "red"
                    self.LeftRotate(w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = "black"
                w.left.color = "black"
                self.RightRotate(x.parent)
                x = self.root
        x.color = "black"

    def LeftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def RightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def TreeMinimum(self, x):
        while(x.left != None):
            x = x.left
        return x

    def __str__(self):
        self.InorderTreeWalk(self.root)
        return ""
