#This assignment was done by a group
#Group Members: Bruce Reier, Jake Terrill
def match(w: str, start: int, end: int, non_terminal: str) -> bool:
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
            if match(w, start, split-1, 'B') and match(w, split, end, 'A'):
                return True
            
        elif non_terminal == 'B':
            if match(w, start, split-1, 'C') and match(w, split, end, 'C'):
                return True
            
        elif non_terminal == 'C':
            if match(w, start, split-1, 'A') and match(w, split, end, 'B'):
                return True
            
    return False
"""
PART 2 WRITTEN RESPONSE:
Based on the nature of recursive parsing, the the maximum time 
it might take for a grammar to determine if a string of length
n belongs to the language is O(2^n). The recursive parser has
many layers of work that add up exponentially as it parses 
a language. The parser checks wether a substring can be generated 
by a specific non terminal in the grammar, and for any given substring 
it tries all possible splits. A split is where it divides the substring 
into two parts and checks to see if there is a rule from the grammar that
can generate the two parts from the starting non terminal given. For a substring 
of length n, there are n-1 ways to split it into two non epsilon strings. Once the 
split is made, each part of the split then recursively does the same and considers 
all possible splits of itself - the substring of the original. The number of calls
grows exponentially with each depth of recursion, where the number of recursive 
calls doubles with each additional split. We know it doubles since we are spitting
into two parts. The total number of recursive calls (which explore all possible splits)
is what primarily drives the O(2^n) complexity. Thus, the maximum time it might take is O(2^n).

"""
def improved_match(w, start: int, end: int, non_terminal: str) -> True:
    s1 = w[start - 1: end]
    n = len(s1)
    cyk = [[set() for _ in range(j)] for j in range(n, 0, -1)] 

    grammar_dict = {
        'AB': {'S', 'C'},
        'BC': {'S'},
        'BA': {'A'}, 
        'a': {'A', 'C'}, 
        'CC': {'B'}, 
        'b': {'B'}
        }

    for i in range(n):
        if s1[i] in grammar_dict:
            cyk[0][i] = grammar_dict[s1[i]]

    for row in range(1, n): 
        for i in range(n - row): 
            for k in range(row): 
                left_part = cyk[k][i]  
                right_part = cyk[row-k-1][i+k+1] 
                for B in left_part:
                    for C in right_part:
                        if B+C in grammar_dict:
                            cyk[row][i] |= grammar_dict[B+C]
    
    return non_terminal in cyk[-1][0]

look_ahead = None
input_stream = None
parsing_success = True

def match2(expected):
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
        H2()
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
