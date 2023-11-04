# Libraries import
import networkx as nx
import matplotlib.pyplot as plt


# Finite automaton creating function
def create_finite_automaton(states, alphabet, transition_function, start_state, accept_states):
    return {'states': states, 'alphabet': alphabet, 'transition_function': transition_function,
            'start_state': start_state, 'accept_states': accept_states}


# Finite automaton processing function
def process(finite_state_machine, word):
    current_state = finite_state_machine['start_state']
    for symbol in word:
        if symbol in finite_state_machine['alphabet']:
            current_state = finite_state_machine['transition_function'][(current_state, symbol)]
        else:
            return False
    return current_state in finite_state_machine['accept_states']


# Plot creating function
def create_plot(fa, title):
    graph = nx.DiGraph()
    graph.add_nodes_from(fa['states'])
    for (state, symbol), next_state in fa['transition_function'].items():
        graph.add_edge(state, next_state, label=symbol)
    position = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, position, cmap=plt.get_cmap('jet'), node_color=[
        'green' if state == fa['start_state'] else 'red' if state in fa['accept_states'] else 'black' for state in
        graph.nodes], node_size=500)
    nx.draw_networkx_labels(graph, position)
    nx.draw_networkx_edges(graph, position, edge_color='black', arrows=True)
    nx.draw_networkx_edge_labels(graph, position,
                                 edge_labels={(u, v): d['label'] for u, v, d in graph.edges(data=True)})
    plt.title(title)
    plt.figtext(0.10, 0.02, "Green: Start State", color='green')
    plt.figtext(0.40, 0.02, "Red: Accept States", color='red')
    plt.figtext(0.70, 0.02, "Black: Other States", color='black')
    plt.show()


# Deterministic finite automaton
states1 = {'q0', 'q1'}
alphabet1 = {'0', '1'}
transition_function1 = {('q0', '0'): 'q0', ('q0', '1'): 'q1', ('q1', '0'): 'q1', ('q1', '1'): 'q1'}
start_state1 = 'q0'
accept_states1 = {'q1'}
dfa = create_finite_automaton(states1, alphabet1, transition_function1, start_state1, accept_states1)

# Nondeterministic finite automaton
states2 = {'q0', 'q1', 'q2', 'q3'}
alphabet2 = {'0', '1'}
transition_function2 = {('q0', '0'): 'q1', ('q0', '1'): 'q0', ('q1', '0'): 'q2', ('q1', '1'): 'q3', ('q2', '0'): 'q2',
                        ('q2', '1'): 'q0', ('q3', '0'): 'q1', ('q3', '1'): 'q3'}
start_state2 = 'q0'
accept_states2 = {'q2', 'q3'}
nfa = create_finite_automaton(states2, alphabet2, transition_function2, start_state2, accept_states2)

# e-Nondeterministic finite automaton
states3 = {'q0', 'q1'}
alphabet3 = {'0', '1', 'ε'}
transition_function3 = {('q0', '0'): 'q0', ('q0', '1'): 'q1', ('q0', 'ε'): 'q1', ('q1', '0'): 'q1', ('q1', '1'): 'q0',
                        ('q1', 'ε'): 'q0'}
start_state3 = 'q0'
accept_states3 = {'q0'}
e_nfa = create_finite_automaton(states3, alphabet3, transition_function3, start_state3, accept_states3)

# DFA test
print("DFA Test 1 - Expected Output: True, Actual Output:", process(dfa, '0101'))
print("DFA Test 2 - Expected Output: False, Actual Output:", process(dfa, '0000'))
create_plot(dfa, "DFA")

# NFA test
print("NFA Test 1 - Expected Output: True, Actual Output:", process(nfa, '100'))
print("NFA Test 2 - Expected Output: True, Actual Output:", process(nfa, '101'))
print("NFA Test 3 - Expected Output: False, Actual Output:", process(nfa, '11'))
create_plot(nfa, "NFA")

# e-NFA test
print("e-NFA Test 1 - Expected Output: True, Actual Output:", process(e_nfa, '101'))
print("e-NFA Test 2 - Expected Output: False, Actual Output:", process(e_nfa, '111'))
create_plot(e_nfa, "e-NFA")
