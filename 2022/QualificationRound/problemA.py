## Problem A: SecondHands
from collections import Counter

data_path = 'Data/second_hands_validation_input.txt'
f = open(data_path,'r')

def SecondHands(case):
    noOfParts, CaseSpace = map(int, f.readline().split())
    styles = list(map(int, f.readline().split()))
    styles = set(styles)

    # styles = Counter(list)
    bucket1 = []
    bucket2 = []

    if (CaseSpace * 2) < noOfParts:
        return "NO"

    for part in styles:
        if (part not in bucket1) or (len(bucket1) < CaseSpace):
            # print(bucket1)
            bucket1.append(part)
        elif (part not in bucket2) or (len(bucket2) < CaseSpace):
            # print(bucket2)
            bucket2.append(part)
        else:
            return "NO"

    return "YES"

cases = int(f.readline())
for c in range(cases):
    print(f'Case #{c+1}: {SecondHands(c+1)}')