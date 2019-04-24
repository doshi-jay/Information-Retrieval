inverted_index = {}


def delta(positions):
    for i in range(len(positions) - 1, 0, -1):
        positions[i] = positions[i] - positions[i-1]
    return positions


with open('inverted_list_unigram.txt','r') as f:
    lines = list(f.readlines())
    for line in lines:
        line = line.split(" -> ")
        positions = line[1].strip()
        positions = positions.replace(" ", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "")
        positions = [int(position) for position in positions.split(",")]
        new_positions = []
        index = 1
        doc_positions = []
        new_position = []
        while index < len(positions):
            start = index + 1
            end = start + int(positions[index])
            doc_positions = positions[start: end]
            doc_positions = delta(doc_positions)
            new_position.append(positions[index - 1])
            new_position.append(positions[index])
            new_position.append(doc_positions)
            new_positions.append(new_position)
            new_position = []
            index = end + 1 
        inverted_index[line[0].strip()] = new_positions
        

output = open('inverted_list_unigram_delta_encoding.txt', 'w+')
for term in inverted_index:
    output.write("%s -> %s\n" %(term , inverted_index[term]))
output.close()
