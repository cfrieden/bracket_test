from collections import deque

def unbalenced(input):
    #python double ended queue allows for poping like a stack and a queue 
    open = deque()
    #travse over string with index
    for idx,c in enumerate(input):
        #if open bracket push index onto queue
        if c == '{':
            open.append(idx)
        elif c == '}':
            # if close bracket and no stored open return idx of first unmatched close
            if len(open) == 0:
                return idx
            #else pop the matched open from right end of deque
            open.pop()
    #if perfectly matched deque will be empty and return -1
    if len(open) == 0:
        return -1
    #else return the first unmatched open bracket (left end of deque)
    else :
        return open.popleft()
