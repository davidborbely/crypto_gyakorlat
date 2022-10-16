from enigma.machine import EnigmaMachine # note: has to be installed, pip install py-enigma
import string
import itertools


alphabet = string.ascii_uppercase # uppercase alphabet
all_startpositions = itertools.product(alphabet, repeat=3) # all 26^3 possible start ring positions

rotors = ['I', 'II', 'III', 'IV', 'V']
all_rotors = itertools.product(rotors, repeat=3) # all 125 possible rotor combinations


# exercise 1
msg = 'aaaaa'.upper()
desired_secret = 'eqdir'.upper()
for sp in all_startpositions:
    engine = EnigmaMachine.from_key_sheet(
        rotors = 'I V III',
        reflector = 'B', 
        ring_settings = [0, 0, 0]
    )
    engine.set_display(sp) # set start position
    if engine.process_text(msg) == desired_secret:
        print(sp)
        break

# exercise 2
msg = 'aaaaa'.upper()
desired_secret = 'eeeek'.upper()
for r in all_rotors: # (26**3)*(8**3) ~ 10M, can be ran on modern computers
    for sp in all_startpositions:
        engine = EnigmaMachine.from_key_sheet(
        rotors = ' '.join(r),
        reflector = 'B', 
        ring_settings = [0, 0, 0]
        )
        engine.set_display(sp)

        if engine.process_text(msg) == desired_secret:
            print(r)
            print(sp)
            
            break