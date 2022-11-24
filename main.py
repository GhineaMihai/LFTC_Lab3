if __name__ == '__main__':
    final = []
    states = []
    transitions = []
    alphabet = []
    f = open("test.txt", "r")

    for line in f:
        lis = line.split("->")                  # split the line in two
        statement = lis[0]                      # first part of the transition
        state = lis[1]                          # second part of the transition
        t = str(statement[1] + statement[2])    # statement[1] = q statement[2] is a digit
        if t not in states:                     # first part
            states.append(t)                    # add the state to the states list if it is not already there
            if statement[0] == "[":             # statement[0] is always {, ( or (
                final.append(t)                 # add the state to the final list if statement[0] = [ (if the state is final)
        t = str(state[1] + state[2])            # state[1] = q state[2] is a digit
        if t not in states:                     # second part
            states.append(t)                    # same as the first part
            if state[0] == "[":                 #
                final.append(t)                 #
        t = str(line[1] + line[2] + " -> " + line[9] + line[10])    # line[1] is q, line[2] is a digit, same for line[9] and line[10]
        if t not in transitions:                #
            transitions.append(t)               # add the transition to the transitions list
        t = str(line[5])                        # line[5] is the alphabet (letter or digit)
        if t not in alphabet:                   #
            alphabet.append(t)                  # add that to the alphabet list

    print("All states: " + str(states))
    print("Final states: " + str(final))
    print("All transitions: " + str(transitions))
    print("Alphabet list: " + str(alphabet))
