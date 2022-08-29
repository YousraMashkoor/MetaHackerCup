## Problem A: SecondHands
from collections import Counter

data_path = 'Data/second_hands_input.txt'
f = open(data_path,'r')

def SecondHands(case):
    noOfParts, CaseSpace = map(int, f.readline().split())
    styles = list(map(int, f.readline().split()))

    style_count = Counter(styles)

    if (CaseSpace * 2) < noOfParts:
        return "NO"
    if (any(c >= 3 for c in style_count.values())):
        return "NO"

    return "YES"

cases = int(f.readline())
for c in range(cases):
    print(f'Case #{c+1}: {SecondHands(c+1)}')