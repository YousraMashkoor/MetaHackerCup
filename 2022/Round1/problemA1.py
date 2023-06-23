## Problem A: SecondHands
from collections import Counter
from utils import CircularQueue, LinkedList

data_path = 'Data/consecutive_cuts_chapter_1_input.txt'
# data_path = 'Data/specialcases.txt'
f = open(data_path,'r')
fw = open('ans.txt', 'w')

def ConsecutiveCuts(case):
    cardsLength, cuts = map(int, f.readline().split())
    startSeq = list(map(int, f.readline().split()))
    endSeq = list(map(int, f.readline().split()))
    
    if startSeq == endSeq:
        if cuts ==1:
            return "NO"
        elif len(startSeq) == 2 and cuts%2: # len == 2 and cuts == odd
            return "NO"

    elif startSeq != endSeq:
        if cuts == 0:
            return "NO"
        elif len(startSeq) == 2 and not cuts%2: # len == 2 and cuts == even
            return "NO"
         

    startQueue = LinkedList()
    endQueue = LinkedList()
    for card in startSeq:
        startQueue.insertNode(card)
    for card in endSeq:
        endQueue.insertNode(card)
    
    # if startQueue.checkIdentical(endQueue) != startQueue.checkIdenticalNew(endQueue):
    #     print('*************Uhoh!! case: ', case)

    if startQueue.checkIdentical(endQueue):
        return "YES"
    else:
        return "NO"

    

cases = int(f.readline())
for c in range(cases):
    fw.write(f'Case #{c+1}: {ConsecutiveCuts(c+1)}')
    fw.write('\n')