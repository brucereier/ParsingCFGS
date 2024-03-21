def match(w: str, start: int, end: int, non_terminal: str) -> bool:
    #print(str(start) + " " + str(end) + " " + str(non_terminal))
    if start == end:
        if non_terminal == 'A':
            return w[start-1] == 'a'
        elif non_terminal == 'B':
            return w[start-1] == 'b'
        elif non_terminal == 'C':
            return w[start-1] == 'a'
        return False
    
    for split in range(start + 1, end + 1):
        #print(split)
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
            return w[start-1] == 'a'
        return False
    
    for split in range(start + 1, end + 1):
        if non_terminal == 'S':
            if (match(w, start, split-1, 'A') and match(w, split, end, 'B')) or (match(w, start, split-1, 'B') and match(w, split, end, 'C')):
                return True
            
        elif non_terminal == 'A':
            if w[start - 1:end] in dpa:
                return True
            if match(w, start, split-1, 'B') and match(w, split, end, 'A'):
                dpa.append(w)
                return True
            
        elif non_terminal == 'B':
            if w[start - 1:end] in dpb:
                return True
            if match(w, start, split-1, 'C') and match(w, split, end, 'C'):
                dpb.append(w)
                return True
            
        elif non_terminal == 'C':
            if w[start - 1:end] in dpc:
                return True
            if match(w, start, split-1, 'A') and match(w, split, end, 'B'):
                dpc.append(w)
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
    #print(look_ahead)
    if look_ahead == '1':
        match2('1')
        OZ()
        match2('0')
        S()
    elif look_ahead == '0':
        match2('0')
        ZO()
        match2('1')
        S()

def ZO():
    if look_ahead == "0":
        match2('0')
        ZO()
        match2('1')
    else:
        return
    
def OZ():
    if look_ahead == "1":
        match2('1')
        OZ()
        match2('0')
    else:
        return

def parser_1(w: str) -> bool:
    reset_globals()
    #print(w)
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
    reset_globals()
    print(w)
    global input_stream, parsing_success
    input_stream = iter(w + "$")
    parsing_success = True

    read_next_char()
    S2()

    return look_ahead == "$" and parsing_success

def S2():
    Z3()
    H2()
    Z3()

def H2():
    if look_ahead == '1':
        match2('1')
        Z3()
        J2()
        Z3()
        match2('1')

def J2():
    if look_ahead == '1':
        match2('1')
        Z3()
        J3()
        Z3()
        match2('1')
    else:
        match2('#')
def parser_3(w: str) -> bool:
    reset_globals()
    rev = w[::-1]
    global input_stream, parsing_success
    input_stream = iter(rev + "$")
    parsing_success = True

    read_next_char()
    S3()

    return look_ahead == "$" and parsing_success

def S3():
    global parsing_success
    if look_ahead == '1':
        match2('1')
        J3()
        match2('0')
        match2('0')
        Z3()
    elif look_ahead != '0':
        return
    else:
        parsing_success = False

def Z3():
    if look_ahead == '0':
        match2('0')
        Z3()

def J3():
    if look_ahead == '1':
        match2('1')
        J3()
        match2('0')
        match2('0')
    else:
        return
w = ""
print(parser_2(w))