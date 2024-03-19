def match(w: str, start: int, end: int, non_terminal: str) -> bool:
    if start == end - 1:
        if non_terminal == 'A':
            return w[start] == 'a'
        elif non_terminal == 'B':
            return w[start] == 'b'
        elif non_terminal == 'C':
            return w[start] == 'c'
        return False  
    for split in range(start + 1, j):
        if non_terminal == 'S':
            if (match(w, start, split, 'A') and match(w, split, end, 'B')) or (match(w, start, split, 'B') and match(w, split, end, 'C')):
                return True

        elif non_terminal == 'A':
            if match(w, start, split, 'B') and match(w, split, end, 'A'):
                return True

        elif non_terminal == 'B':
            for split in range(start + 1, j):
                if match(w, start, split, 'C') and match(w, split, end, 'C'):
                    return True

        elif non_terminal == 'C':
            if match(w, start, split, 'A') and match(w, split, end, 'B'):
                return True

    return False

dpa = []
dpb = []
dpc = []
def improved_match(w: str, start: int, end: int, non_terminal: str) -> bool:
    if start == end - 1:
        if non_terminal == 'A':
            return w[start] == 'a'
        elif non_terminal == 'B':
            return w[start] == 'b'
        elif non_terminal == 'C':
            return w[start] == 'c'
        return False  
    for split in range(start + 1, end):
        if non_terminal == 'S':
            if (match(w, start, split, 'A') and match(w, split, end, 'B')) or (match(w, start, split, 'B') and match(w, split, end, 'C')):
                return True

        elif non_terminal == 'A':
            if w[start:split] in dpa:
                return True
            if match(w, start, split, 'B') and match(w, split, end, 'A'):
                dpa.append(w[start:end])
                return True

        elif non_terminal == 'B':
            if w[start:split] in dpb:
                return True
            for split in range(start + 1, end):
                if match(w, start, split, 'C') and match(w, split, end, 'C'):
                    dpb.append(w[start:end])
                    return True

        elif non_terminal == 'C':
            if w[start:split] in dpb:
                return True
            if match(w, start, split, 'A') and match(w, split, end, 'B'):
                dpc.append(w[start:end])
                return True

    return False