import sys

filePath = sys.argv[1]

def main():
    with open(filePath, "r+") as inputFile:
        for exp in inputFile:
            expression = exp.rstrip().split(' ')
            stack = []
            answers = []
            for l in reversed(expression):
                if l.isdigit():
                    stack.insert(0,int(l))
                else:
                    if l == '+':
                        result = stack.pop(0) + stack.pop(0)
                        stack.insert(0,result)
                    elif l == '-':
                        result = stack.pop(0) - stack.pop(0)
                        stack.insert(0,result)
                    elif l == '/':
                        result = stack.pop(0) / stack.pop(0)
                        stack.insert(0,result)
                    elif l == '*':
                        result = stack.pop(0) * stack.pop(0)
                        stack.insert(0,result)
                    else:
                        print("Invalid Lexicon Found")
            print stack.pop(0)

if __name__ == '__main__':
    main()
