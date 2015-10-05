import sys

filePath = sys.argv[1]

def main():
    with open(filePath, "r+") as inputFile:
        for A in inputFile:
            s = A.index(';');
            k = int(A[:s])
            A = list(map(int, list(A[s+1:-1].split(' '))))
            ksum = A[0]
            for i in range(1, k):
                ksum += A[i]
            maxsum = ksum
            maxend = k-1
            for i in range(k, len(A)):
                ksum += A[i]
                ksum -= A[i - k]
                if ksum > maxsum:
                    maxsum = ksum
                    maxend = i
            if maxsum > -1:
                print(maxsum)
            else:
                print('0')

if __name__ == '__main__':
    main()
