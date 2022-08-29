## Problem A: SecondHands
from collections import Counter

data_path = 'Data/second_friend_input.txt'
f = open(data_path,'r')
fw = open('ans.txt', 'w')

def makeFriends(rows, col):
    sol = []
    for r in range(rows):
        sol.append("^"*col)
    return "\n".join(sol)

def readIt():
    """
    decides if it needs to skip a line or read it from file.
    resets the pointer to the line it wants to read
    """
    last_pos = f.tell()
    line = f.readline()
    if not (line[0] == '.' or line[0] == '^'):
        f.seek(last_pos)
        return
    else:
        line = readIt()

def SecondFriend(case):
    readIt()
    rows, col = map(int, f.readline().split())
    
    if col == 1:
        for r in range(rows):
            if f.readline().strip('\n') == "^":
                return "Impossible", ""
        return "Possible", '\n'+'\n'.join(("." for x in range(rows)))
    elif rows == 1:
        painting = f.readline()
        if "^" in painting:
            return "Impossible", ""
        return "Possible", '\n'+painting.strip('\n')
    return "Possible",'\n'+ makeFriends(rows, col)


cases = int(f.readline())
for c in range(cases):
    ans, sol = SecondFriend(c+1)
    fw.write(f'Case #{c+1}: {ans}')
    if ans == 'Possible':
        fw.write(sol)
    fw.write('\n')