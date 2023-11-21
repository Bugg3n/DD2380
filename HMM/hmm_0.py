import sys

def format_input():
    input_lines = sys.stdin.readlines()  # Read all lines from stdin
    i = 0
    input_list = []
    for line in input_lines:
        input_list.append(line.strip().split(" "))   # Split each line into list elements

    
    matrixes = [[] for _ in range(len(input_list))]

    for j in range(len(input_list)):
        rows = int(input_list[j][0])  # Convert to integer
        row_length = int(input_list[j][1])  # Convert to integer
        for i in range(rows):
            print(i)
            print(j)
            matrix_row = input_list[j][2 + i*row_length:2+(i+1)*row_length]  # Slice the correct portion for each row
            matrixes[j].append(matrix_row)
    
    return matrixes

matrixes = format_input()
print(matrixes[0])
print(matrixes[1])
print(matrixes[2])

# Example usage
# transition_matrix = format_input()
# print(transition_matrix)




def hmm(transition, emission, initial_state):
    # multiply transition matrix with current estimate of states.
    for i in transition:
        for j in transition[i]:
            transition[i][j] = transition[i][j]*initial_state[i] # Ingen aning om detta är korrekt

