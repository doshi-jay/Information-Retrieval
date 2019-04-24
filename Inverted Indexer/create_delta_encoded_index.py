inverted_index = {}

filename = 'inverted_list_trigram.txt'
# Function to generate delta encoding of the list
def delta(positions):
    for i in range(len(positions) - 1, 0, -1):
        positions[i] = positions[i] - positions[i-1]
    return positions


# Read the inverted indices from the file
with open(filename,'r') as f:
    lines = list(f.readlines())
    for line in lines:
        # Split on term, values
        line = line.split(" -> ")
        positions = line[1].strip()
        # Create a simple list of numbers, eventhough in string 
        positions = positions.replace(" ", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "")
        # Creating a list splitting on ","
        positions = [int(position) for position in positions.split(",")]
        new_positions = []
        # Keep track of position in the list
        index = 1
        # positions at which the word can be found
        doc_positions = []
        new_position = []
        # Loop through the positions list
        while index < len(positions):
            # Start defines the start of occurence positions in the list
            start = index + 1
            # En defines the end of occurence positions in the list
            end = start + int(positions[index])
            doc_positions = positions[start: end]
            doc_positions = delta(doc_positions)
            # Create temporary variable to store the entries
            new_position.append(positions[index - 1])
            new_position.append(positions[index])
            new_position.append(doc_positions)
            new_positions.append(new_position)
            # Reset temporary variable
            new_position = []
            # Move index to the right
            index = end + 1 
        # Append to the list
        inverted_index[line[0].strip()] = new_positions
        

# Open file to write to it
output = open('inverted_list_trigram_delta_encoding.txt', 'w')
for term in inverted_index:
    # Write to the file
    output.write("%s -> %s\n" %(term , inverted_index[term]))
output.close()
