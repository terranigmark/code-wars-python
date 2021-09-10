def solution(string, ending):
    # your code here...
    if string[-len(ending):] == ending or ending == '':
        return True
    else:
        return False