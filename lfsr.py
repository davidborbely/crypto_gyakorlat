initial_state = '11011110'
desired_result = '01010101'

# XOR lambda
xor2 = lambda a, b : str(int(bool(int(a)) ^ bool(int(b))))
def xor(*args):
    current_value = args[0]
    for arg in args[1:]:
        current_value = xor2(current_value, arg)
    return current_value


# XOR at positions to get next elem, and push to the start of the sequence
def step(state, *positions):
    # get values to be xored
    values = [state[p] for p in positions]

    return xor(*values) + state[:-1]

def step_8(initial_state, *positions):
    state = initial_state
    for i in range(8):
        state = step(state, *positions)
    return state

def print_result(*positions):
    print(f'The positions that need to be XOR\'d together to get the desired output, indexed from 0:\n{positions}')

# try all positions and see which one corresponds to the given output
for pos1 in range(8):
    for pos2 in range(pos1+1, 8):
        for pos3 in range(pos2+1, 8):
            for pos4 in range(pos3+1, 8):
                for pos5 in range(pos4+1, 8):
                    for pos6 in range(pos5+1, 8):
                        for pos7 in range(pos6+1, 8):
                            for pos8 in range(pos7+1, 8):
                                if step_8(initial_state, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8) == desired_result:
                                    print_result(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8)
                            if step_8(initial_state, pos1, pos2, pos3, pos4, pos5, pos6, pos7) == desired_result:
                                print_result(pos1, pos2, pos3, pos4, pos5, pos6, pos7)
                        if step_8(initial_state, pos1, pos2, pos3, pos4, pos5, pos6) == desired_result:
                            print_result(pos1, pos2, pos3, pos4, pos5, pos6)
                    if step_8(initial_state, pos1, pos2, pos3, pos4, pos5) == desired_result:
                        print_result(pos1, pos2, pos3, pos4, pos5)
                if step_8(initial_state, pos1, pos2, pos3, pos4) == desired_result:
                    print_result(pos1, pos2, pos3, pos4)
            if step_8(initial_state, pos1, pos2, pos3) == desired_result:
                print_result(pos1, pos2, pos3)
        if step_8(initial_state, pos1, pos2) == desired_result:
            print_result(pos1, pos2)
                
