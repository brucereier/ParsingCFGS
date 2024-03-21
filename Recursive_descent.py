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


def improved_match2(w: str, start: int, end: int, non_terminal: str) -> bool:
    # Assuming term_dict is defined outside this function
    global term_dict

    # Create a 2D array with specific values
    width_height = len(w)
    array_2d = [[width_height - row for _ in range(width_height)] for row in range(width_height)]

    row_to_modify = width_height - 1 
    for col in range(len(w)):
        char = w[col]
        if char in term_dict:
            array_2d[row_to_modify][col] = term_dict[char]

    # Skip the last row (first in iteration) by adjusting the range in the outer loop
    for row in reversed(range(width_height - 1)):  # Start from the second last row
        for col in range(width_height - (width_height - 1 - row)):
            # Checking if the element is a list (from term_dict) or an integer
            if isinstance(array_2d[row][col], list):
                print(array_2d[row][col], end=' ')
            else:
                print(array_2d[row][col], end=' ')
        print()  # Newline after each row

    # Placeholder for the actual matching logic, should return a boolean
    return True

def improved_match(w, start: int, end: int, non_terminal: str) -> True:
    print(w)
    print(start)
    print(end)
    s1 = w[start - 1: end]
    print(s1)
    n = len(s1)
    dp = [[set() for _ in range(n+1)] for _ in range(n+1)]
    
    # Convert grammar for easy access
    grammar_dict = {}
    for left, rights in grammar.items():
        for right in rights:
            if right not in grammar_dict:
                grammar_dict[right] = set()
            grammar_dict[right].add(left)

    # Base case: fill in single characters
    for i in range(1, n+1):
        if s1[i-1] in grammar_dict:
            dp[i][i] = grammar_dict[s1[i-1]]
    
    # Fill the table
    for length in range(2, n+1):  # Substring lengths
        for i in range(1, n-length+2):  # Start of substring
            j = i+length-1  # End of substring
            for k in range(i, j):  # Position to split the substring
                for B in dp[i][k]:
                    for C in dp[k+1][j]:
                        if B+C in grammar_dict:
                            dp[i][j] |= grammar_dict[B+C]
    
    # Check if 'S' is in the start of the full string
    return 'S' in dp[1][n]

grammar = {
    'S': {'AB', 'BC'},
    'A': {'BA', 'a'},
    'B': {'CC', 'b'},
    'C': {'AB', 'a'},
}
term_dict = {
    "a": ["A", "C"],
    "b": ["B"]
}

nonterm_dict = {
    "AA" : [],
    "AB" : ["S", "C"],
    "AC" : [],
    "BA" : ["A"],
    "BB" : [],
    "BC" : ["S"],
    "CA" : [],
    "CB" : [],
    "CC" : ["B"],
}
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
w = ""
print(improved_match("aabab", 1, 1, "A"))