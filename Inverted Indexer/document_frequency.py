inverted_index = {}

is_unigram = False
# Decode the delta encoded inverted list
def decode(positions):
    for i in range(1, len(positions)):
        positions[i] = positions[i] + positions[i-1]
    return positions

# Open file to read delta encoded inverted indices
with open('inverted_list_trigram.txt','r') as f:
    lines = list(f.readlines())
    for line in lines:
        # Split to make key, value pairs
        line = line.split(" -> ")
        positions = line[1].strip()
        # Create a simple list of numbers, eventhough in string 
        positions = positions.replace(" ", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "")
        # Creating a list splitting on ","
        positions = [int(position) for position in positions.split(",")]
        new_positions = []
        # Keep track of position in the list
        index = 1
        # positions ar which the can be found
        doc_positions = []
        new_position = []
        terms = 0
        # Loop through the positions list
        while index < len(positions):
            # Start defines the start of occurence positions in the list
            start = index + 1
            # End defines the end of occurence positions in the list
            end = start + int(positions[index])
            doc_positions = positions[start: end]
            if is_unigram:
                doc_positions = decode(doc_positions)
            new_position.append(positions[index - 1])
            new_position.append(positions[index])
            new_positions.append(new_position)
            new_position = []
            # Move index to the right
            index = end + 1 
        # Append to the list
        inverted_index[line[0].strip()] = new_positions


import collections

# Sort the inverted indices based on keys
inverted_index = collections.OrderedDict(sorted(inverted_index.items()))

# Open file to write
output = open('document_frequency_table_trigram.txt', 'w')
for term in inverted_index:
    # Write each term with its frequency
    output.write(str(term) + ": " + str(inverted_index[term]) + "\n")
output.close()


