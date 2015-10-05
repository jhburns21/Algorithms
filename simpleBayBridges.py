import sys
from ast import literal_eval
import itertools
import operator


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

def main():
    filePath = sys.argv[1]
    bridges = []
    points = []
    with open(filePath, "r+") as inputFile:
        for s in inputFile:
            x = literal_eval(s)
            x = [tuple(elem) for elem in x]
            bridges.append(x)
    #store intersections
    done = False
    answer = list(range(len(bridges)))
    while(not(done)):
        intersect = dict(zip(range(len(bridges)), [0]*len(bridges)))
        counta = 0
        for a in bridges:
            countb = 0
            for b in bridges:
                if counta == countb:
                    countb+=1
                    continue
                else:
                    if SegmentsIntersect(a[0], a[1], b[0], b[1]):
                        intersect[counta]+=1
                        intersect[countb]+=1
                        countb+=1
            counta+=1
        if(all(val==0 for val in intersect.values())):
            done=True
        else:
            maxKey = max(intersect.items(), key=operator.itemgetter(1))[0]
            bridges.pop(maxKey)
            answer.pop(maxKey)

    for x in answer:
        print(x)



if __name__ == '__main__':
    main()
