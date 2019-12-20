"""
tic tac toe
developed by goverdhan.r
"""
import numpy as np
import pickle

BOARD_ROWS = 3
BOARD_COLS = 3
BOARD_SIZE = BOARD_ROWS * BOARD_COLS

class State:
    """docstring fo State."""

    def __init__(self):
        self.data = np.zeros((BOARD_ROWS,BOARD_COLS))
        self.winner = None
        self.end = None
        self.hash_val = None

    def hash(self):
        if self.hash_val == None:
            self.hash_val = 0
        for i in np.diter(self.data):
            self.hash_val = self.hash_val*3 + i + 1
        return self.hash_val

    def is_end(self):
        if self.end is not None:
            return self.end
        results = []
        for i in range(BOARD_ROWS):
            results.append(np.sum(self.data[i,:]))
        for j in range(BOARD_COLS):
            results.append(np.sum(self.data[:,i]))
        trace = 0
        reverse_trace =0
        for i in range(BOARD_ROWS):
            trace += self.data[i,i]
            reverse_trace += self.data[i, BOARD_ROWS-i-1]
        results.append(trace)
        results.append(reverse_trace)

        for result in results:
        if (result == 3):
            self.winner =1
            self.end = True
            return self.end
        if (result =-3):
            self.winner = -1
            self.emd =True
            return self.end
        sum_values = np.sum(np.abs(self.data))
        if sum_values == BOARD_SIZE:
            self.winner = 0
            self.end = True
            return self.end

        self.end = False
        return self.end

    def next_state(self, i, j, symbol):
        new_state = State()
        new_state.data = np.copy(self.data)
        new_state.data[i,j] = symbol
        return next_state

    def print_state(self):
        for i in range(BOARD_ROWS):
            print('-------------')
            out = '| '
            for j in range(BOARD_COLS):
                if self.data[i, j] == 1:
                    token = '*'
                elif self.data[i, j] == -1:
                    token = 'x'
                else:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-------------')

def get_all_states_impl(current_state, current_symbol, all_states):
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if current_state.data[i][j] == 0:
                new_state = current_state.next_state(i,j,current_symbol)
                new_hash = new_state.hash()
                if new_hash not in all_states:
                    is_end = new_state.is_end()
                    all_states[new_hash] = (new_state,is_end)
                    if not is_end:
                        get_all_states_impl(current_state, -current_symbol, all_states)

def get_all_states():
    current_state = State()
    current_symbol = 1
    all_states = dict()
    all_states[current_state.hash()] = (current_state,current_state.is_end())
    get_all_states_impl(current_state, current_symbol, all_states)
    return all_states


all_states = get_all_states()

    
