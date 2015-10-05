import sys
from ast import literal_eval

# accepts tuples as p
def SegmentsIntersect(p1, p2, p3, p4):
    d1 = Direction(p3, p4, p1)
    d2 = Direction(p3, p4, p2)
    d3 = Direction(p1, p2, p3)
    d4 = Direction(p1, p2, p4)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 ==0 and OnSegment(p3, p4, p1):
        return True
    elif d1 ==0 and OnSegment(p3, p4, p2):
        return True
    elif d1 ==0 and OnSegment(p1, p2, p3):
        return True
    elif d1 ==0 and OnSegment(p1, p2, p4):
        return True
    else:
        return False

def Direction(pi, pj, pk):
    return (pk[0]-pi[0])*(pj[1]-pi[1]) - (pj[0]-pi[0])*(pk[1] - pi[1])

def OnSegment(pi, pj, pk):
    if ((min(pi[0], pj[0]) <= pk[0]) and (pk[0] <= max(pi[0], pj[0]))) and ((min(pi[1], pj[1]) <= pk[1]) and (pk[1] <= max(pi[1], pj[1]))):
        return True
    else:
        return false

class RBNode:
    def __init__(self, p, val):
        self.left = None
        self.right = None
        self.value = val
        self.parent = p
        self.color = "red"

class RBTree:
    def __init__(self):
        nil = RBNode(None, None)
        nil.color = "black"
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
        xoriginal = x
        while x != None and not(k == x.value):
            if k[0][1] < x.value[0][1]:
                x = x.left
            else:
                x = x.right
        return x

    def DetermineCross(self, pi, pj, pk):
        return (pk[0]-pi[0])*(pj[1]-pi[1]) - (pj[0]-pi[0])*(pk[1] - pi[1])

    def RBInsert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if self.DetermineCross(x.value[0],x.value[1],z.value[0]) < 0:
                x = x.right
            else:
                x = x.left
        z.parent = y
        if y == None:
            self.root = z
        elif self.DetermineCross(y.value[0],y.value[1],z.value[0]) < 0:
            y.right = z
        else:
            y.left = z
        z.left = None
        z.right = None
        z.color = "red"
        self.RBInsertFix(z)

    def RBInsertFix(self, z):
        while z.parent != None and z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y != None and y.color == "red":
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
        if v != None:
            v.parent = u.parent
        else:
            pass

    def RBDelete(self, z):
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
        if x != None:
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

    def Above(self, x):
        y = self.IterativeTreeSearch(self.root, x)
        if(y != None and y.right != None):
            return y.right
        else:
            return False

    def Below(self, x):
        y = self.IterativeTreeSearch(self.root, x)
        if(y != None and y.left != None):
            return y.left
        else:
            return False

    def __str__(self):
        self.InorderTreeWalk(self.root)
        return ""

def sortPoints(B):
    sortedList = []
    for b in B:
        if sortedList == []:
            sortedList.append(b)
            continue
        index = 0
        for p in sortedList:
            if b[0] > p[0]:
                index+=1
            elif b[0] < p[0]:
                break
            elif b[0] == p[0]:
                #tie
                if b[2] == 'l' and p[2] == 'r':
                    break
                elif b[2] == 'r' and p[2] == 'l':
                    index+=1
                elif (b[2] == 'l' and p[2] == 'l') or (b[2] == 'r' and p[2] == 'r'):
                    if b[1] < p[1]:
                        break
                    elif b[1] > p[1]:
                        index+=1
                    else:
                        break
        sortedList.insert(index, b)
        index = 0
    return sortedList

def findBridge(B, p):
    for b in B:
        if b[0][0] == p[0] and b[0][1] == p[1]:
            return b

def findBridgeR(B, p):
    for b in B:
        if b[1][0] == p[0] and b[1][1] == p[1]:
            return b

def main():
    filePath = sys.argv[1]
    bridges = []
    points = []
    tree = RBTree()
    with open(filePath, "r+") as inputFile:
        for s in inputFile:
            x = literal_eval(s)
            x = [tuple(elem) for elem in x]
            bridges.append(x)

    for t in bridges:
        points.append((t[0][0], t[0][1], 'l'))
        points.append((t[1][0], t[1][1], 'r'))

    points = sortPoints(points)

    for p in points:
        if p[2] == 'l':
            b = findBridge(bridges, p)
            tree.RBInsert(RBNode(None, b))
            above = tree.Above(b)
            below = tree.Below(b)
            print(above)
            print(below)
            print(tree)
            if ((above != False and SegmentsIntersect(b[0], b[1], above[0], above[1])) or (below != False and SegmentsIntersect(b[0], b[1], below[0], below[1]))):
                print("Intersection!")
        if p[2] == 'r':
            b = findBridgeR(bridges, p)
            above = tree.Above(b)
            below = tree.Below(b)
            print(above)
            print(below)
            print(tree)
            if ((above != False and below != False) and (SegmentsIntersect(above[0], above[1], below[0], below[1]))):
                print("Intersection!")
            tree.RBDelete(tree.IterativeTreeSearch(tree.root, b))


    print("done")

if __name__ == '__main__':
    main()
