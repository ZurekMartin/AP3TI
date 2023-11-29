# Library import
import re


# Finite automaton creating function
def create_finite_automaton(states, alphabet, transition_function, start_state, accept_states):
    return {'states': states, 'alphabet': alphabet, 'transition_function': transition_function,
            'start_state': start_state, 'accept_states': accept_states}


# Finite automaton processing function
def process(finite_state_machine, string):
    current_state = finite_state_machine['start_state']
    for symbol in string:
        if symbol in finite_state_machine['alphabet']:
            current_state = finite_state_machine['transition_function'][(current_state, symbol)]
        else:
            return False
    return current_state in finite_state_machine['accept_states']


# Function for checking if string is in format of regular expression
def check_format(string, regular_expression):
    regular_expression = regular_expression.replace('#', '[0-9]')
    regular_expression = regular_expression.replace('$', '[a-zA-Z]')
    regular_expression = regular_expression.replace('&', '[a-zA-Z0-9]')
    states = set('q' + str(i) for i in range(len(string) + 1))
    alphabet = set(string)
    transition_function = {}
    for i in range(len(string)):
        transition_function[('q' + str(i), string[i])] = 'q' + str(i + 1)
    start_state = 'q0'
    accept_states = {'q' + str(len(string))}
    finite_automaton = create_finite_automaton(states, alphabet, transition_function, start_state, accept_states)
    if re.fullmatch(regular_expression, string):
        return process(finite_automaton, string)
    else:
        return False


# Email format checking
print("Format checking: str: name@email.c0m, reg: &&*@&&*.$$$*")
print(check_format("name@email.c0m", "&*@&*.$$$*"))  # False
print("Format checking: str: name@email.com, reg: &&*@&&*.$$$*")
print(check_format("name@email.com", "&*@&*.$$$*"))  # True

# Phone number format checking
print("Format checking: str: 777mkd530, reg: #########")
print(check_format("777mkd530", "#########"))  # False
print("Format checking: str: 777640530, reg: #########")
print(check_format("777640530", "#########"))  # True
