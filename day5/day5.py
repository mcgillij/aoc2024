def parse_input(ordering_rules):
    rules = {}
    for rule in ordering_rules:
        x, y = map(int, rule.split('|'))
        if x not in rules:
            rules[x] = set()
        rules[x].add(y)
    return rules

def is_valid_sequence(sequence, rules):
    for i in range(len(sequence) - 1):
        if sequence[i + 1] not in rules.get(sequence[i], []):
            return False
    return True

def filter_sequences(sequences, ordering_rules):
    rules = parse_input(ordering_rules)
    valid_sequences = []
    invalid_sequences = []
    for sequence in sequences:
        if is_valid_sequence(sequence, rules):
            valid_sequences.append(sequence)
        else:
            invalid_sequences.append(sequence)
    return valid_sequences, invalid_sequences

def read_input(input_str):
    # Split the input by '\n\n' to separate ordering rules and sequences
    parts = input_str.strip().split('\n\n')
    
    # The first part contains the ordering rules
    ordering_rules = parts[0].strip().split('\n')
    
    # The second part contains the sequences
    sequences = []
    for seq in parts[1].strip().split('\n'):
        sequences.append([int(num) for num in seq.split(',')])

    return ordering_rules, sequences


def get_middle_element(sequence):
    return sequence[len(sequence) // 2]


def sort_sequences(sequences, rules):
    order_map = parse_input(rules)
    
    sorted_sequences = []
    for sequence in sequences:
        sorted_sequence = topological_sort(sequence, order_map)
        if not sorted_sequence:  # If sorting fails (e.g., due to cycles), keep the original
            sorted_sequences.append(sequence)
        else:
            sorted_sequences.append(sorted_sequence)
    
    return sorted_sequences

def topological_sort(sequence, order_map):
    from collections import defaultdict
    
    # Create a dictionary to store the in-degree of each node
    in_degree = {node: 0 for node in sequence}
    
    # Update in-degrees based on the order map
    for before, afters in order_map.items():
        if before in sequence:
            for after in afters:
                if after in sequence:
                    in_degree[after] += 1
    
    # Initialize a queue with nodes that have zero in-degree
    queue = [node for node in sequence if in_degree[node] == 0]
    sorted_sequence = []
    
    while queue:
        node = queue.pop(0)
        sorted_sequence.append(node)
        
        # Decrease the in-degree of adjacent nodes and add them to the queue if they become zero
        for before, afters in order_map.items():
            if before == node:
                for after in afters:
                    if after in sequence:
                        in_degree[after] -= 1
                        if in_degree[after] == 0:
                            queue.append(after)
    
    # If the sorted sequence is not the same length as the original, there was a cycle
    if len(sorted_sequence) != len(sequence):
        return None
    
    return sorted_sequence

order, seqs = read_input(open('test_input').read())
#order, seqs = read_input(open('day5_input').read())
valid_sequences, invalid = filter_sequences(seqs, order)
new_invalid = sort_sequences(invalid, order)

my_list = [get_middle_element(x) for x in valid_sequences]
my_list2 = [get_middle_element(x) for x in new_invalid]

# end
part1 = sum(my_list)
print(f"{part1=}")
part2 = sum(my_list2)
print(f"{part2=}")
