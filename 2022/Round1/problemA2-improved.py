from collections import Counter
from utils import LinkedList

data_path = 'Data/consecutive_cuts_chapter_2_input_practice.txt'
# data_path = 'Data/test-chapter2.txt'
f = open(data_path,'r')
fw = open('ans.txt', 'w')

def ConsecutiveCuts(case):
    cardsLength, cuts = map(int, f.readline().split())
    startSeq = list(map(str, f.readline().split()))
    endSeq = list(map(str, f.readline().split()))

    print(case)

    if startSeq == endSeq:
        if cuts ==1:
            return "NO"
        elif cardsLength == 2 and cuts%2: # len == 2 and cuts == odd
            return "NO"

    elif startSeq != endSeq:
        if cuts == 0:
            return "NO"
        elif cardsLength == 2 and not cuts%2: # len == 2 and cuts == even
            return "NO"


    # SOLUTION 2
    # main = ''.join(endSeq)+''.join(endSeq)
    # substring = ''.join(startSeq)

    # if substring in main:
    #     return "YES"
    # else:
    #     return "NO"

    # SOLUTION 3
    startQueue = LinkedList()
    endQueue = LinkedList()
    for card in startSeq:
        startQueue.insertNode(card)
    for card in endSeq:
        endQueue.insertNode(card)
    
    # if startQueue.checkIdentical(endQueue) != startQueue.checkIdenticalNew(endQueue):
    #     print('*************Uhoh!! case: ', case)
    if startQueue.checkIdenticalNew(endQueue):
        return "YES"
    else:
        return "NO"

#2:26 2:30
    

cases = int(f.readline())
import time
start_time = time.time()
for c in range(cases):
    fw.write(f'Case #{c+1}: {ConsecutiveCuts(c+1)}')
    fw.write('\n')

end_time = time.time()
print(end_time - start_time)