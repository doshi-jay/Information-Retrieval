inverted_index = {}

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
        print positions
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
            terms += positions[index]
            # Move index to the right
            index = end + 1 
        # Append to the list
        inverted_index[line[0].strip()] = terms


import operator

# Sort the inverted indices
inverted_index = sorted(inverted_index.items(), key=operator.itemgetter(1))[::-1]

# Open file to write
output = open('stop_list_trigram.txt', 'w')
for term in inverted_index:
    # Write each term with its frequency
    output.write(str(term) + "\n")
output.close()


