inverted_index = {}


def delta(positions):
    for i in range(len(positions), 0, -1):
        positions[i] = positions[i] - positions[i-1]
    return positions


with open('inverted_list_unigram.txt','r') as f:
    lines = f.readlines()
    for line in lines[2]:
        print line
        line = line.split(" -> ")
        positions = line[1].strip()
        positions = positions.replace(" ", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "")
        index = 1
        while index < len(positions):
            start = index + 1
            end = start + positions[index]
            doc_positions = positions[start: end]
            doc_positions = delta(doc_positions)
            index = end + 2  
        inverted_index[line[0].strip()] = line[1].strip()


print inverted_index
