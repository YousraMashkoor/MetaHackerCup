import time
from utils import LinkedList

data_path = 'Data/consecutive_cuts_chapter_2_input_practice.txt'
# data_path = 'Data/test-chapter2.txt'
f = open(data_path,'r')
fw = open('ans.txt', 'w')

def ConsecutiveCuts(case):
    cardsLength, cuts = map(int, f.readline().split())
    startSeq = list(map(str, f.readline().split()))
    endSeq = list(map(str, f.readline().split()))

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

    startQueue = LinkedList()
    endQueue = LinkedList()
    for card in startSeq:
        startQueue.insertNode(card)
    for card in endSeq:
        endQueue.insertNode(card)

    if startQueue.checkIdenticalNew(endQueue):
        return "YES"
    else:
        return "NO"
    

cases = int(f.readline())
start_time = time.time()
for c in range(cases):
    cuts = ConsecutiveCuts(c+1)
    print(f'Case #{c+1}: {cuts}')
    fw.write(f'Case #{c+1}: {cuts}')
    fw.write('\n')

end_time = time.time()
print(end_time - start_time)

'''
NOTE: 
very inefficient, this solution took __ minutes

'''