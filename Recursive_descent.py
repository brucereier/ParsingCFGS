def match(w: str, start: int, end: int, non_terminal: str) -> bool:
    if start == end:
        if non_terminal == 'A':
            return w[start-1] == 'a'
        elif non_terminal == 'B':
            return w[start-1] == 'b'
        elif non_terminal == 'C':
            return w[start-1] == 'c'
        return False
    
    for split in range(start + 1, end + 1):
        if non_terminal == 'S':
            if (match(w, start, split-1, 'A') and match(w, split, end, 'B')) or (match(w, start, split-1, 'B') and match(w, split, end, 'C')):
                return True
            
        elif non_terminal == 'A':
            if match(w, start, split-1, 'B') and match(w, split, end, 'A'):
                return True
            
        elif non_terminal == 'B':
            if match(w, start, split-1, 'C') and match(w, split, end, 'C'):
                return True
            
        elif non_terminal == 'C':
            if match(w, start, split-1, 'A') and match(w, split, end, 'B'):
                return True
            
    return False

dpa = []
dpb = []
dpc = []
def improved_match(w: str, start: int, end: int, non_terminal: str) -> bool:
    if start == end:
        if non_terminal == 'A':
            return w[start-1] == 'a'
        elif non_terminal == 'B':
            return w[start-1] == 'b'
        elif non_terminal == 'C':
            return w[start-1] == 'c'
        return False
    
    for split in range(start + 1, end + 1):
        if non_terminal == 'S':
            if (match(w, start, split-1, 'A') and match(w, split, end, 'B')) or (match(w, start, split-1, 'B') and match(w, split, end, 'C')):
                return True
            
        elif non_terminal == 'A':
            if w[start - 1:end] in dpa:
                return True
            if match(w, start, split-1, 'B') and match(w, split, end, 'A'):
                return True
            
        elif non_terminal == 'B':
            if w[start - 1:end] in dpb:
                return True
            if match(w, start, split-1, 'C') and match(w, split, end, 'C'):
                return True
            
        elif non_terminal == 'C':
            if w[start - 1:end] in dpc:
                return True
            if match(w, start, split-1, 'A') and match(w, split, end, 'B'):
                return True
            
    return False

#w = "bbb"
#print(improved_match(w, 1, len(w), "S"))

look_ahead = None
input_stream = None
parsing_success = True

def match2(expected):
    print(expected)
    global look_ahead, parsing_success
    if look_ahead == expected:
        read_next_char()
    else:
        parsing_success = False

def read_next_char():
    global look_ahead, input_stream
    try:
        look_ahead = next(input_stream)
    except StopIteration:
        look_ahead = None

def S():
    if look_ahead == '1':
        match2('1')
        if look_ahead in ('0', '1'):
            S()  # Continue parsing after matching '1'
        match2('0')
    elif look_ahead == '0':
        match2('0')
        if look_ahead in ('0', '1'):
            S()  # Continue parsing after matching '0'
        match2('1')
    else:
        return

def parser_1(w: str) -> bool:
    global input_stream, parsing_success
    input_stream = iter(w + "$")
    parsing_success = True

    read_next_char()
    S()

    return look_ahead == "$" and parsing_success

def reset_globals():
    global look_ahead, input_stream, parsing_success
    look_ahead = None
    input_stream = None
    parsing_success = True

def parser_2(w: str) -> bool:
    print(w)
    return False

def parser_3(w: str) -> bool:
    print(w)
    return False
print(parser_1("0101"))